# Generated by Django 2.0 on 2018-02-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='width_field',
        ),
    ]
