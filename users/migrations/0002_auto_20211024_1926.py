# Generated by Django 3.2.8 on 2021-10-24 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 19, 26, 33, 473939)),
        ),
        migrations.AlterField(
            model_name='reader',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 24, 19, 26, 33, 473939)),
        ),
    ]