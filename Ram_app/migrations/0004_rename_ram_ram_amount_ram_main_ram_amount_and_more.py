# Generated by Django 5.1.2 on 2024-11-03 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ram_app', '0003_rename_description_ram_main_ram_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ram_main',
            old_name='ram_ram_amount',
            new_name='ram_amount',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='ram_ram_size',
            new_name='ram_size',
        ),
    ]
