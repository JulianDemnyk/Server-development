# Generated by Django 5.1.2 on 2024-11-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Motherboard_app', '0002_rename_motherboard_motherboard_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='description',
            new_name='motherboard_description',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='form_factor',
            new_name='motherboard_form_factor',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='m2_slot',
            new_name='motherboard_m2_slot',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='manufacturer',
            new_name='motherboard_manufacturer',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='name',
            new_name='motherboard_name',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='ram_type',
            new_name='motherboard_ram_type',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='sata_slot',
            new_name='motherboard_sata_slot',
        ),
        migrations.RenameField(
            model_name='motherboard_main',
            old_name='socket_motherboard',
            new_name='motherboard_socket_motherboard',
        ),
    ]