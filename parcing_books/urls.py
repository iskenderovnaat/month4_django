from django.urls import path
from . import views

urlpatterns = [
    path('books_list/', views.BooksListView.as_view(), name='books_list'),
    path('books_parser/', views.BooksFormView.as_view(), name='books_parser'),
]