# Generated by Django 3.1.4 on 2021-01-04 22:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('switches', '0015_log_if_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='switch',
            old_name='snmp_hostname',
            new_name='hostname',
        ),
    ]
