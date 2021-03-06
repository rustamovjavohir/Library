# Generated by Django 3.2.8 on 2021-11-02 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20211031_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='read_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 22, 25, 26, 804497)),
        ),
        migrations.AlterField(
            model_name='kartoteka',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 22, 25, 26, 804497)),
        ),
        migrations.AlterField(
            model_name='kartoteka',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 17, 22, 25, 26, 810499)),
        ),
    ]
