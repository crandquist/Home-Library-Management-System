from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import ReadingLog
from .forms import ReadingLogForm

class ReadingLogListView(ListView):
    model = ReadingLog
    context_object_name = 'reading_logs'

class ReadingLogCreateView(CreateView):
    model = ReadingLog
    form_class = ReadingLogForm
    success_url = reverse_lazy('reading_log_list')

class ReadingLogUpdateView(UpdateView):
    model = ReadingLog
    form_class = ReadingLogForm
    success_url = reverse_lazy('reading_log_list')

