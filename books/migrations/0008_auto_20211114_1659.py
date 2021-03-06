# Generated by Django 3.2.8 on 2021-11-14 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20211103_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cost',
            field=models.IntegerField(default=20000),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kartoteka',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='kartoteka',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 29, 16, 59, 17, 353071)),
        ),
    ]
