# Generated by Django 3.1.1 on 2020-09-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0012_auto_20200913_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='summ',
            field=models.FloatField(default=0),
        ),
    ]
