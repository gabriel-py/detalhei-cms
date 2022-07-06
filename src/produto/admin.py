from django.contrib import admin
from django_stisla.admin import site
from .models import Produto, Categoria, Subcategoria, Topico, Nota, NotaItens
from django.shortcuts import redirect
from django.urls import reverse_lazy



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'categoria')


# class TopicoAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'peso', 'subcategoria',)

class TopicoInline(admin.StackedInline):
    extra = 0
    model = Topico

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'categoria')

    inlines = [
        TopicoInline
    ]


class NotaItensInline(admin.StackedInline):
    model = NotaItens
    readonly_fields = ('topico', 'valor_calculado')
    extra = 0
    max_num = 0

    def has_delete_permission(self, request, obj=None):
        return False


class NotaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'data')
    inlines = (NotaItensInline,)

    def save_model(self, request, obj, form, change):
        if not change:
            subcategorias = obj.produto.categoria.subcategorias.all()
            topicos = Topico.objects.filter(subcategoria__in=subcategorias)
            obj.save()

            for topico in topicos:
                NotaItens.objects.create(nota=obj, topico=topico)

        super(NotaAdmin, self).save_model(request, obj, form, change)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect(reverse_lazy('admin:produto_nota_change', kwargs={'object_id': obj.id}))  # noqa E501

site.register(Produto, ProdutoAdmin)
site.register(Subcategoria, SubcategoriaAdmin)
# site.register(Topico, TopicoAdmin)
site.register(Nota, NotaAdmin)
site.register(Categoria)

