# Generated by Django 5.1.1 on 2024-10-30 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(blank=True, default='no-email.fde08c8f572f4a05aed87cf48f5cd0cd@noemail.com', max_length=254, null=True, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.genero', verbose_name='Genero'),
        ),
    ]