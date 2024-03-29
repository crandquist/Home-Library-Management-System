from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

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
    published = models.IntegerField(
        validators=[
            MinValueValidator(1800),
            MaxValueValidator(datetime.datetime.now().year)
        ],
        help_text="Use the format: YYYY"
    )
    pages = models.PositiveIntegerField()
    read = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=1, choices=FORMAT_CHOICES, default='H')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author}"
