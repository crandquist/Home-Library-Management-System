from django.urls import path
from . import views

urlpatterns = [
    path('add-book/', views.add_book, name='add_book'),
    path('book/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('mybooks/', views.user_books, name='user_books'),
]
