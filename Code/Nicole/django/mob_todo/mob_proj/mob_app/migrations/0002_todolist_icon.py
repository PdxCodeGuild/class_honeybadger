# Generated by Django 2.2.6 on 2019-11-07 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mob_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='icon',
            field=models.CharField(default='keyboard_arrow_right', max_length=20),
            preserve_default=False,
        ),
    ]
