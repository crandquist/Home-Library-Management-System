from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import DetailView
from .forms import LibraryForm, BookForm
from .models import Library

@login_required
def create_library(request):
    if request.method == 'POST':
        form = LibraryForm(request.POST)
        if form.is_valid():
            library = form.save(commit=False)
            library.created_by = request.user
            library.save()
            return redirect(reverse('library_detail', kwargs={'library_id': library.id}))
    else:
        form = LibraryForm()
    return render(request, 'library_app/create_library.html', {'form': form})


@login_required
def add_book(request, library_id):
    library = Library.objects.get(id=library_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.library = library
            book.save()
            messages.success(request, "Book added successfully.")
            return redirect('library_detail', library_id=library.id)
    else:
        form = BookForm(initial={'library': library})
    return render(request, 'library_app/add_book.html', {'form': form, 'library': library})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_app/library_detail.html'
    context_object_name = 'library'
    pk_url_kwarg = 'library_id'