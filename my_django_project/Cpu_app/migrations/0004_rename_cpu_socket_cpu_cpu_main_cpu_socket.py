# Generated by Django 5.1.2 on 2024-11-03 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cpu_app', '0003_rename_cores_cpu_main_cpu_cores_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cpu_main',
            old_name='cpu_socket_cpu',
            new_name='cpu_socket',
        ),
    ]
