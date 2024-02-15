from django import forms
from .models import Book
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class BookForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the book title'
        }),
        help_text="The full title of the book as it appears on the cover.",
        label="Book Title"
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Author name'
        }),
        help_text="Full name of the book's author.",
        label="Author"
    )
    isbn = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '13-digit ISBN'
        }),
        help_text="The 13-digit International Standard Book Number without hyphens.",
        label="ISBN"
    )
    published = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Year'
        }),
        help_text="The year the book was published. Use the format: YYYY",
        label="Published Year",
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    pages = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of pages'
        }),
        help_text="Total number of pages in the book.",
        label="Pages"
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published', 'pages']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        # Initialize your form fields' querysets or choices here if needed.
