from django.contrib import admin
from .models import Book

# Optional: Define a custom admin class to customize the admin interface
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published', 'read', 'owner')
    list_filter = ('read', 'format', 'published', 'owner')
    search_fields = ('title', 'author', 'isbn')

# Register your models here.
admin.site.register(Book, BookAdmin)
