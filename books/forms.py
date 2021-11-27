from django import forms
from .models import Book, Kartoteka


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'picture', 'count', 'category']


class KartotekaForm(forms.ModelForm):
    class Meta:
        model = Kartoteka
        fields = ['reader', 'book', 'return_date']

