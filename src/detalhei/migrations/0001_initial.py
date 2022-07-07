# Generated by Django 3.0.8 on 2022-07-07 02:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontos_fortes', jsonfield.fields.JSONField()),
                ('pontos_fracos', jsonfield.fields.JSONField()),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('custo_beneficio', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Area')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('has_the_product', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador_comentario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('logo', models.TextField()),
                ('url_site_loja', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('video_url', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('peso', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Seguidores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seguidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_que_segue', to=settings.AUTH_USER_MODEL)),
                ('seguindo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_que_eh_seguido', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Revisao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pontos_fortes', jsonfield.fields.JSONField()),
                ('pontos_fracos', jsonfield.fields.JSONField()),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Area')),
            ],
        ),
        migrations.CreateModel(
            name='PostEngajamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(choices=[('like', 'Curtiu o post'), ('favorito', 'Favoritou o post'), ('compartilhar', 'Compartilhou o post')], db_index=True, default='like', max_length=100)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Produto'),
        ),
        migrations.CreateModel(
            name='Opiniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('gostei', models.CharField(max_length=180)),
                ('gostaria', models.CharField(max_length=180)),
                ('eh_recomendada', models.BooleanField()),
                ('eh_verificada', models.BooleanField()),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Loja')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='NotaAvaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Avaliacao')),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Topico')),
            ],
        ),
        migrations.CreateModel(
            name='Descricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas', jsonfield.fields.JSONField()),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Setor')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioEngajamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(choices=[('like', 'Curtiu o comentário'), ('favorito', 'Favoritou o comentário')], db_index=True, default='like', max_length=100)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Comentario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='response_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='detalhei.Comentario'),
        ),
        migrations.AddField(
            model_name='avaliacao',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Post'),
        ),
        migrations.AddField(
            model_name='area',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detalhei.Departamento'),
        ),
    ]