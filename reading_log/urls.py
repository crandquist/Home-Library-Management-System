from django.urls import path
from . import views

urlpatterns = [
    path('user-reading-log/', views.user_reading_log, name='user_reading_log'),
    path('add/', views.add_reading_log, name='reading_log_add'),
]
