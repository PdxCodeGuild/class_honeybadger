# Generated by Django 2.2.7 on 2019-11-13 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('favnumapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favnum',
            name='other_reason',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='favnum',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='fav_nums', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
