# Generated by Django 5.1.1 on 2024-09-17 16:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.UUID('870a42fc-cb59-4672-ac86-234c5ba1f40e'), primary_key=True, serialize=False),
        ),
    ]