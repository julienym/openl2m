# Generated by Django 3.2.8 on 2021-10-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('switches', '0029_auto_20211004_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commandtemplate',
            name='template',
            field=models.CharField(
                help_text='The command template. Use {{field[1-8]}} or {{list[1-5]}} as needed.',
                max_length=512,
                verbose_name='Command Template',
            ),
        ),
    ]
