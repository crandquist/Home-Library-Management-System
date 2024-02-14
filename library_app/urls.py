from django.urls import path
from . import views

urlpatterns = [
    path('create_library/', views.create_library, name='create_library'),
    path('add_book/<int:library_id>/', views.add_book, name='add_book'),
]
