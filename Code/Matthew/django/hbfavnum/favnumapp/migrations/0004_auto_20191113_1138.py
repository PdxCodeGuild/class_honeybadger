# Generated by Django 2.2.7 on 2019-11-13 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('favnumapp', '0003_auto_20191113_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favnum',
            old_name='reasons',
            new_name='reason',
        ),
    ]
