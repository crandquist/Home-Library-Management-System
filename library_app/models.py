from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    FORMAT_CHOICES = [
        ('H', 'Hardcover'),
        ('P', 'Paperback'),
        ('A', 'Audiobook'),
        ('E', 'Ebook'),
        ('O', 'Other')
    ]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published = models.DateField()
    read = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=1, choices=FORMAT_CHOICES, default='H')
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"

