# Generated by Django 3.0.8 on 2022-07-08 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalhei', '0003_auto_20220708_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sumario',
            name='ranking',
        ),
    ]
