from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from sendEmail.views import send_activation_link
from .forms import ReaderForm, EmployeeForm
from .models import Reader, Token, Employee
from .service.utils import checking_password, checking_employee, user_update_, get_user_


@transaction.atomic
def employee_create(request):
    if request.method == 'POST':
        data = EmployeeForm(request.POST, request.FILES).data
        img = request.FILES.get('picture')
        user = User(username=data.get('username'), first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    email=data.get('email'), password=make_password(data.get('password')), is_staff=1)
        user.save()
        Employee(user=user, phone=data.get('phone'), picture=img).save()
        return redirect('books:book_list')
    form = EmployeeForm()
    context = {'form': form}
    return render(request, template_name='registration.html', context=context)


@transaction.atomic
def registration(request):
    if request.method == 'POST':
        data = ReaderForm(request.POST, request.FILES).data
        img = request.FILES.get('picture')
        if checking_password(data.get('password'), data.get('re_password')):
            user = User(username=data.get('username'), first_name=data.get('first_name'),
                        last_name=data.get('last_name'),
                        email=data.get('email'), password=make_password(data.get('password')))
            user.save()
            Reader(user=user, phone=data.get('phone'), picture=img, card=data.get('card'),
                   profession=data.get('profession')).save()
        return redirect('users:_login')
    form = ReaderForm()
    context = {'form': form}
    return render(request, template_name='registration.html', context=context)


def _login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, template_name='index.html')
        messages.error(request=request, message='Bad credentials')
    return render(request, template_name='login.html', context={})


def _logout(request):
    logout(request)
    return redirect('home:home')


def personal_cabinet(request):
    name = request.GET.get('search', '')

    reader = request.user.reader
    books = reader.kartoteka_set.all()
    if name:
        books = books.filter(Q(book__title__icontains=name) | Q(book__author__icontains=name))
    page = request.GET.get('page', 1)
    pagination = Paginator(books, 3)
    books = pagination.page(page)
    context = {'books': books}
    if request.user.is_staff:
        user = checking_employee(request)
        context = {'books': books, 'user': user}
    return render(request, template_name='personal_cabinet.html', context=context)


def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        user = User.objects.filter(username=username).first()
        if user.email.__eq__(email):
            send_activation_link(user)
            return render(request, template_name='reset_dane.html', context={'have': True})
        return render(request, template_name='reset_dane.html', context={'have': False})
    return render(request, template_name='reset_password.html')


def verify_user(request):
    token = request.GET.get('token')
    _token = Token.objects.get(token=token, is_delete=0)
    if _token:
        user = _token.user
        return new_password_page(request, user)
    return HttpResponse('This token is invalid')


def new_password_page(request, user):
    if request.method == 'POST':
        new_password(username=user.username, password=request.POST.get('password', ''))
        return redirect('users:_login')
    return render(request, template_name='new_password.html')


def new_password(username, password):
    user = User.objects.filter(username=username)
    user.update(password=make_password(password))


def user_update(request):
    form = get_user_(request.user.pk)
    if request.method == 'POST':
        user_update_(request, request.user.pk)
        return redirect('users:personal_cabinet')
    return render(request, template_name='update_user.html', context=form)
