import datetime
from os.path import join as join_path

from django.contrib.auth.models import User
from django.db import models

from books.service.utils import BookType
from users.models import Abstract, Reader


class Book(Abstract):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=join_path('books', 'picture'))
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=BookType.choice())
    count = models.IntegerField(default=1)
    cost = models.IntegerField(default=20000)
    read_count = models.IntegerField(default=0)
    stars = models.IntegerField(default=0)
    book_file = models.FileField(upload_to=join_path('books', 'files'), null=True, blank=True)

    def __str__(self):
        return self.title.capitalize()


class Kartoteka(Abstract):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    return_date = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=15)))

    def __str__(self):
        return f'{self.reader.user.get_username()}<-->{self.book.title}'
