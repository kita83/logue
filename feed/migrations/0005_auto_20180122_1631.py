# Generated by Django 2.0 on 2018-01-22 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20180120_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='item_cd',
        ),
        migrations.RemoveField(
            model_name='like',
            name='type_cd',
        ),
    ]
