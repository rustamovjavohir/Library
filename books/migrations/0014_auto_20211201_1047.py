# Generated by Django 3.2.8 on 2021-12-01 05:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_auto_20211201_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_file',
            field=models.FileField(default='path', upload_to='books\\file'),
        ),
        migrations.AlterField(
            model_name='kartoteka',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 16, 10, 47, 27, 618447)),
        ),
    ]
