# Generated by Django 2.2.6 on 2019-11-12 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20191112_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='slug',
        ),
    ]
