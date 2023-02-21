# Generated by Django 4.1.5 on 2023-02-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[[10, 'DEBUG'], [20, 'Information'], [25, 'Success'], [30, 'Warning'], [40, 'Error']], default=30, help_text='Proirity of this notice, as defined by Message Levels', verbose_name='Notice priority'),
        ),
    ]
