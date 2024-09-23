# Generated by Django 5.0.9 on 2024-09-21 01:13

import django_resized.forms
import usuarios.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='avatar',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[736, 736], unique=True, upload_to=usuarios.models.generar_nombre, verbose_name='Avatar'),
        ),
    ]