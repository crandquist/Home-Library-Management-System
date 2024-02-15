from django.urls import path
from . import views
from .views import LibraryDetailView, add_book, edit_book, delete_book

urlpatterns = [
    path('create_library/', views.create_library, name='create_library'),
    path('library/<int:library_id>/add_book/', add_book, name='add_book_to_library'),
    path('library_detail/<int:library_id>/', LibraryDetailView.as_view(), name='library_detail'),
    path('book/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('book/delete/<int:book_id>/', delete_book, name='delete_book'),
]
