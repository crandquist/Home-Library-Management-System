from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ReadingLog
from .forms import ReadingLogForm

@login_required
def user_reading_log(request):
    # Initialize the form with the current user
    if request.method == 'POST':
        form = ReadingLogForm(request.POST, user=request.user)
        if form.is_valid():
            reading_log = form.save(commit=False)
            reading_log.user = request.user
            reading_log.save()
            return redirect('reading_log:user_reading_log')
    else:
        form = ReadingLogForm(user=request.user)  # Pass the user here as well
    logs = ReadingLog.objects.filter(user=request.user).order_by('-date_read')
    return render(request, 'reading_log/user_reading_log.html', {'form': form, 'logs': logs})

@login_required
def add_reading_log(request):
    if request.method == 'POST':
        form = ReadingLogForm(request.POST, user=request.user)  # Pass the user here
        if form.is_valid():
            reading_log = form.save(commit=False)
            reading_log.user = request.user  # Set the current user
            reading_log.save()  # Now you can save the ReadingLog
            return redirect('reading_log:user_reading_log')  # Redirect to a new URL
    else:
        form = ReadingLogForm(user=request.user)  # Initialize form with the current user

    return render(request, 'reading_log/add_reading_log.html', {'form': form})
