# Generated by Django 2.1.5 on 2019-10-25 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatingPreference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DatingProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='datingprofile',
            name='genders',
            field=models.ManyToManyField(to='bapp.Gender'),
        ),
        migrations.AddField(
            model_name='datingprofile',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bapp.Location'),
        ),
        migrations.AddField(
            model_name='datingprofile',
            name='preferences',
            field=models.ManyToManyField(to='bapp.DatingPreference'),
        ),
    ]