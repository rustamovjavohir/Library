import datetime
from os.path import join as join_path

from django.contrib.auth.models import User
from django.db import models


class Abstract(models.Model):
    created_by = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.IntegerField(default=0)
    updated_at = models.DateTimeField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Reader(Abstract):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to=join_path('reader', 'picture'))
    profession = models.CharField(max_length=200)
    card = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user.get_username()}'


class Employee(Abstract):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    picture = models.ImageField(upload_to=join_path('employee', 'picture'))
    phone = models.CharField(max_length=12)


class Token(models.Model):
    token = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_delete = models.IntegerField(default=0)
    send_time = models.DateTimeField()

    def __str__(self):
        return self.token
