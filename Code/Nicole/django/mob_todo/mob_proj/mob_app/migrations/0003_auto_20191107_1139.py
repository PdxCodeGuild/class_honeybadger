# Generated by Django 2.2.6 on 2019-11-07 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mob_app', '0002_todolist_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='icon',
            field=models.CharField(max_length=200),
        ),
    ]