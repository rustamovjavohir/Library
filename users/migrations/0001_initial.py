# Generated by Django 3.2.8 on 2021-10-24 14:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 10, 24, 14, 18, 18, 9618, tzinfo=utc))),
                ('is_deleted', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('picture', models.ImageField(upload_to='employee\\picture')),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('created_by', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 10, 24, 14, 18, 18, 9618, tzinfo=utc))),
                ('is_deleted', models.IntegerField(default=0)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('picture', models.ImageField(upload_to='reader\\picture')),
                ('profession', models.CharField(max_length=200)),
                ('card', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]