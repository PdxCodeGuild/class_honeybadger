# Generated by Django 2.2.6 on 2019-10-28 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todopost',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]