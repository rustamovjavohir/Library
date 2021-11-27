import enum
from collections import namedtuple

from django.db.models import F


class BookType(enum.Enum):
    Historical = 'Historical'
    Scientific = 'Scientific'
    Romance = 'Romance'
    ForKids = 'For Kids'
    Literature = 'Literature'

    @classmethod
    def choice(cls):
        return [tuple((item.name, item.value)) for item in cls]

    @staticmethod
    def process():
        sh = namedtuple('a', 'name value')
        _ = list()
        for item in BookType:
            _.append(sh(item.name, item.value))

        return _


def increment_read_book(book_id):
    from books.models import Book
    book = Book.objects.filter(pk=book_id).first()
    book.read_count = F('read_count') + 1
    book.save()
