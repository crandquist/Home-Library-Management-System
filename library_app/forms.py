from django import forms
from .models import Library, Book

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'library']
