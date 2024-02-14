from django.shortcuts import render, redirect
from .forms import LibraryForm, BookForm
from .models import Library

def create_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            library = form.save(commit=False)
            library.created_by = request.user
            library.save()
            return redirect('some-view-name')  # Redirect to a new page
    else:
        form = LibraryForm()
    return render(request, 'your_app/create_library.html', {'form': form})

def add_book(request, library_id):
    library = Library.objects.get(id=library_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.library = library
            book.save()
            return redirect('some-view-name')  # Redirect to a new page
    else:
        form = BookForm(initial={'library': library})
    return render(request, 'your_app/add_book.html', {'form': form, 'library': library})
