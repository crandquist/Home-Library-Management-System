from django.db import models
from django.conf import settings
from library_app.models import Book  # Adjust the import path according to your project structure

class ReadingLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reading_logs')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reading_logs')
    date_read = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} read by {self.user.username} on {self.date_read}"
