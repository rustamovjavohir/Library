from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import BookForm, KartotekaForm
from .models import Book, Kartoteka
from .service import increment_read_book


def book_list(request):
    books = Book.objects.all()
    name = request.GET.get('search', '')
    if name:
        books = Book.objects.filter(Q(title__icontains=name) | Q(author__icontains=name))
    page = request.GET.get('page', 1)
    pagination = Paginator(books, 3)
    books = pagination.page(page)
    context = {'book_list': books}
    return render(request, 'book_list.html', context=context)


@transaction.atomic
@login_required
def book_create(request):
    current_user = request.user
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES.get('picture'))
        book = form.save(commit=False)
        book.created_by = current_user.id
        book.created_at = timezone.now()
        book.save()
        return redirect('books:book_list')
    form = BookForm()
    context = {'form': form}
    return render(request, template_name='book_create.html', context=context)


@transaction.atomic
@login_required
def kartoteka_create(request):
    current_user = request.user
    if request.method == "POST":
        form = KartotekaForm(request.POST, request.FILES)
        kartoteka = form.save(commit=False)
        kartoteka.created_by = current_user.id
        kartoteka.created_at = timezone.now()
        kartoteka.save()
        return redirect('books:book_list')
    form = KartotekaForm()
    context = {'form': form}
    return render(request, template_name='kartoteka_create.html', context=context)


def book_detail(request, pk):
    book = Book.objects.filter(pk=pk).first()
    context = {'book': book}
    user = User.objects.filter(pk=request.user.id).first()
    if request.method == 'POST':
        if user and not user.is_anonymous and not user.is_staff:
            reader = user.reader
            Kartoteka(book=book, reader=reader, created_at=timezone.now(), created_by=reader.user.id).save()
            return redirect('books:book_list')
        else:
            return redirect('users:_login')
    increment_read_book(book_id=pk)
    return render(request, template_name='book_detail.html', context=context)


def book_category(request, category=None):
    if category:
        books = Book.objects.filter(category=category).all()
    else:
        books = Book.objects.all()
    page = request.GET.get('page', 1)
    pagination = Paginator(books, 3)
    books = pagination.page(page)
    context = {'book_list': books}
    return render(request, template_name='book_list.html', context=context)


def book_update(request, pk):
    if request.method == 'POST':
        book = Book.objects.filter(pk=pk).first()
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.picture = request.FILES.get('picture')
        book.count = request.POST.get('count')
        book.cost = request.POST.get('cost')
        book.save()
        return redirect('books:book_detail', pk)
    book = Book.objects.filter(pk=pk).first()
    form = {'title': book.title, 'author': book.author, 'picture': book.picture.url, 'count': book.count,
            'cost': book.cost, 'category': book.category}
    return render(request, template_name='book_update.html', context={'form': form})
