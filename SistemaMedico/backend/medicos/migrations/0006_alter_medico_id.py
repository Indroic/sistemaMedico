# Generated by Django 5.1.1 on 2024-09-17 20:43

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0005_alter_especialidad_especialidad_alter_medico_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id',
            field=models.UUIDField(default=uuid.UUID('862c0b27-6722-492d-beb3-f74321736273'), primary_key=True, serialize=False),
        ),
    ]