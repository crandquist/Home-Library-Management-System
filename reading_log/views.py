from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView
from .models import ReadingLog
from .forms import ReadingLogForm

@login_required
def user_reading_log(request):
    if request.method == 'POST':
        form = ReadingLogForm(request.POST)
        if form.is_valid():
            reading_log = form.save(commit=False)
            reading_log.user = request.user
            reading_log.save()
            return redirect('reading_log:user_reading_log')
    else:
        form = ReadingLogForm()
    logs = ReadingLog.objects.filter(user=request.user).order_by('-date_read')
    return render(request, 'reading_log/user_reading_log.html', {'form': form, 'logs': logs})

@login_required
def add_reading_log(request):
    if request.method == 'POST':
        form = ReadingLogForm(request.POST)
        if form.is_valid():
            reading_log = form.save(commit=False)
            reading_log.user = request.user  # Set the current user
            reading_log.save()  # Now you can save the ReadingLog
            return redirect('reading_log:user_reading_log')  # Redirect to a new URL
    else:
        form = ReadingLogForm()

    return render(request, 'reading_log/add_reading_log.html', {'form': form})

class ReadingLogUpdateView(UpdateView):
    model = ReadingLog
    form_class = ReadingLogForm
    template_name = 'reading_log/readinglog_form.html'
    # Define other necessary attributes and methods

