# Generated by Django 3.0.8 on 2022-07-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('path', models.CharField(max_length=64, unique=True)),
                ('menu_type', models.CharField(choices=[('MODULE', 'Módulo'), ('MENU', 'Menu'), ('PAGE', 'Página')], default='PAGE', max_length=6)),
                ('enabled', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Grupos')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ('path',),
            },
        ),
    ]
