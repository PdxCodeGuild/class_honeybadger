# Generated by Django 2.1.5 on 2019-10-28 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='blogapp.BlogPostCategory'),
        ),
    ]
