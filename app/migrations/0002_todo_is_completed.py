# Generated by Django 4.0.5 on 2022-07-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_completed',
            field=models.BooleanField(default=True),
        ),
    ]
