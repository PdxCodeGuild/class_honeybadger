# Generated by Django 2.2.6 on 2019-10-29 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_00_todo', '0002_auto_20191023_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
