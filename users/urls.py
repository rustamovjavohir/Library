from django.urls import path

from .views import registration, _login, _logout, personal_cabinet, reset_password, verify_user, \
    user_update

app_name = 'users'
urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', _login, name='_login'),
    path('logout/', _logout, name='logout'),
    path('personal_cab/', personal_cabinet, name='personal_cabinet'),
    path('reset_password/', reset_password, name='reset_password'),
    path('verify/', verify_user, name='verify_user'),
    path('update_user/', user_update, name='user_update'),
]
