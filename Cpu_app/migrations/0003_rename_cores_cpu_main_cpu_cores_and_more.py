# Generated by Django 5.1.2 on 2024-11-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cpu_app', '0002_rename_cpu_cpu_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu_main',
            old_name='cores',
            new_name='cpu_cores',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='description',
            new_name='cpu_description',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='manufacturer',
            new_name='cpu_manufacturer',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='name',
            new_name='cpu_name',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='series',
            new_name='cpu_series',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='socket_cpu',
            new_name='cpu_socket_cpu',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='tdp',
            new_name='cpu_tdp',
        ),
        migrations.RenameField(
            model_name='cpu_main',
            old_name='threads',
            new_name='cpu_threads',
        ),
    ]
