from django import forms
from .models import ReadingLog

class ReadingLogForm(forms.ModelForm):
    date_read = forms.DateField(
        input_formats=['%m-%d-%Y'],  # Accepts MM-DD-YYYY format
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YYYY',
            'title': 'Enter the date in MM-DD-YYYY format',
        }, format='%m-%d-%Y'),
        help_text="Format: Month-Day-Year (e.g., 02-14-2024).",
        label="Date Read"
    )
    book = forms.ModelChoiceField(
        queryset=ReadingLog.objects.none(),  # Update this queryset based on your requirements
        help_text="Select the book you read. If you can't find the book, make sure to add it to your book list first.",
        label="Book",
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    notes = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'rows': 4,
            'placeholder': 'Write any notes or thoughts you had about the book here...'
        }),
        help_text="Optional. Add any personal notes or insights about the book.",
        label="Notes",
        required=False
    )

    class Meta:
        model = ReadingLog
        fields = ['book', 'date_read', 'notes']

    def __init__(self, *args, **kwargs):
        # If you need to dynamically set the queryset for books based on the user,
        # you can do so here by popping 'user' from kwargs and filtering the queryset accordingly.
        # Example:
        # user = kwargs.pop('user', None)
        # super(ReadingLogForm, self).__init__(*args, **kwargs)
        # if user is not None:
        #     self.fields['book'].queryset = Book.objects.filter(owner=user)
        super(ReadingLogForm, self).__init__(*args, **kwargs)
        # Initialize your form fields' querysets or choices here if needed.
