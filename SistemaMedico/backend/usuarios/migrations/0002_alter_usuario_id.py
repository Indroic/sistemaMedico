# Generated by Django 5.1.1 on 2024-09-17 16:05

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a9b2f87f-750e-11ef-99e2-f0038c90f80e'), primary_key=True, serialize=False),
        ),
    ]
