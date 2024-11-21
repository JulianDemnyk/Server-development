# Generated by Django 5.1.2 on 2024-11-03 16:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id_ram', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('form_factor', models.CharField(max_length=50)),
                ('ram_size', models.CharField(max_length=50)),
                ('ram_amount', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RamRecomendedBuild',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
