# Generated by Django 2.2 on 2022-03-18 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkStatus3', '0002_auto_20220318_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlerror',
            name='checkUrl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='error', to='checkStatus3.CheckUrl'),
        ),
    ]
