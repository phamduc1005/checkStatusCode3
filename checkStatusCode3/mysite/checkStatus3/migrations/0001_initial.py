# Generated by Django 2.2 on 2022-03-18 02:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=20)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('errors', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UrlError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField()),
                ('url', models.CharField(max_length=200)),
                ('checkUrl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='error', to='checkStatus3.CheckUrl')),
            ],
        ),
    ]
