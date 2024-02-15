from django.urls import path
from .views import ReadingLogListView, ReadingLogCreateView, ReadingLogUpdateView

urlpatterns = [
    path('', ReadingLogListView.as_view(), name='reading_log_list'),
    path('add/', ReadingLogCreateView.as_view(), name='reading_log_add'),
    path('edit/<int:pk>/', ReadingLogUpdateView.as_view(), name='reading_log_edit'),
]
