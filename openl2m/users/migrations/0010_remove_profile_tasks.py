# Generated by Django 4.2.1 on 2023-06-05 23:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_alter_profile_last_ldap_login"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="tasks",
        ),
    ]
