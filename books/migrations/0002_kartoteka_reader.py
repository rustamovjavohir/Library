# Generated by Django 3.2.8 on 2021-10-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kartoteka',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.reader'),
        ),
    ]
