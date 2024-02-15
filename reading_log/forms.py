from django import forms
from .models import ReadingLog

class ReadingLogForm(forms.ModelForm):
    class Meta:
        model = ReadingLog
        fields = ['book', 'date_read', 'notes']  # Make sure these are the actual fields in your ReadingLog model
