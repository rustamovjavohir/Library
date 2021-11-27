from django.urls import path

from books.views import book_list, book_create, kartoteka_create, book_detail, book_category, book_update

app_name = 'books'
urlpatterns = [
    path('list/', book_list, name='book_list'),
    path('create/', book_create, name='book_create'),
    path('kartoteka_create/', kartoteka_create, name='kartoteka_create'),
    path('book_detail/<int:pk>', book_detail, name='book_detail'),
    path('category/<str:category>/', book_category, name='book_category'),
    path('book_update/<int:pk>/', book_update, name='book_update'),
]
