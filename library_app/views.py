from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookForm
from .models import Book

@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user  # Assign the book directly to the logged-in user
            book.save()
            messages.success(request, "Book added successfully.")
            return redirect('library_app:user_books')  # Redirect to the user's book list
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})


@login_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)  # Ensure book belongs to the user
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('user_books')  # Redirect to the list of user's books
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/edit_book.html', {'form': form})

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, owner=request.user)  # Ensure book belongs to the user
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('user_books')  # Redirect to the list of user's books
    return render(request, 'library_app/confirm_delete.html', {'book': book})

@login_required
def user_books(request):
    books = Book.objects.filter(owner=request.user).order_by('date_added')
    context = {'books': books}
    return render(request, 'library_app/user_books.html', context)