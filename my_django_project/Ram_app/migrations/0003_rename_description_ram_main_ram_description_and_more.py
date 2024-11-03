# Generated by Django 5.1.2 on 2024-11-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ram_app', '0002_rename_ram_ram_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ram_main',
            old_name='description',
            new_name='ram_description',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='form_factor',
            new_name='ram_form_factor',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='manufacturer',
            new_name='ram_manufacturer',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='name',
            new_name='ram_name',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='ram_amount',
            new_name='ram_ram_amount',
        ),
        migrations.RenameField(
            model_name='ram_main',
            old_name='ram_size',
            new_name='ram_ram_size',
        ),
        migrations.RenameField(
            model_name='ramrecomendedbuild',
            old_name='id',
            new_name='ram_id',
        ),
    ]