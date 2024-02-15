from django.urls import path
from . import views

urlpatterns = [
    path('user-reading-log/', views.user_reading_log, name='user_reading_log'),
    path('add/', views.ReadingLogCreateView.as_view(), name='reading_log_add'),
    path('edit/<int:pk>/', views.ReadingLogUpdateView.as_view(), name='reading_log_edit'),
]
