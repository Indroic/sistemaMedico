# Generated by Django 5.1.1 on 2024-09-17 16:27

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.UUIDField(default=uuid.UUID('411d9bd5-6e61-482e-b272-ee3736b06c7e'), primary_key=True, serialize=False),
        ),
    ]
