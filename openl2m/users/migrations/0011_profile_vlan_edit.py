# Generated by Django 4.2.2 on 2023-06-14 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_remove_profile_tasks"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="vlan_edit",
            field=models.BooleanField(
                default=False,
                help_text="If VLAN Edit is set, this user can add or edit VLANs on switches.",
                verbose_name="Allow VLAN adding or editing",
            ),
        ),
    ]
