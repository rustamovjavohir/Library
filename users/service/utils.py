from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


def checking_password(password: str, re_password: str):
    return password.__eq__(re_password)


def checking_employee(request):
    user = request.user
    # context = {'user': user}
    return user


def user_update_(request, pk):
    user = User.objects.filter(pk=pk).first()
    user.username = request.POST.get('username')
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    if request.POST.get('password'):
        user.set_password(request.POST.get('password', request.POST.get('password')))
    if user.is_staff:
        user.employee.picture = request.FILES.get('picture', user.employee.picture)
        user.employee.save()
    else:
        user.reader.picture = request.FILES.get('picture', user.reader.picture)
        user.reader.card = request.POST.get('card')
        user.reader.phone = request.POST.get('phone')
        user.reader.profession = request.POST.get('profession')
        user.reader.save()
    user.save()
    login(request, user)


def get_user_(user_id: int):
    user = get_object_or_404(User, id=user_id)
    context = {'username': user.username, 'last_name': user.last_name, 'first_name': user.first_name,
               'email': user.email}
    if user.is_staff:
        add = {'picture': user.employee.picture, 'phone': user.employee.phone}
    else:
        add = {'picture': user.reader.picture, 'phone': user.reader.phone, 'card': user.reader.card,
               'profession': user.reader.profession}
    context.update(add)
    return context
