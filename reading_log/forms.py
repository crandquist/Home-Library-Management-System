from django import forms
from .models import ReadingLog

class ReadingLogForm(forms.ModelForm):
    start_date = forms.DateField(
        input_formats=['%m-%d-%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YYYY',
        }),
        help_text='Format: MM-DD-YYYY',
    )
    end_date = forms.DateField(
        required=False,
        input_formats=['%m-%d-%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'MM-DD-YYYY',
        }),
        help_text='Format: MM-DD-YYYY (optional)',
    )

    class Meta:
        model = ReadingLog
        fields = ['book_title', 'author', 'start_date', 'end_date', 'notes']
        widgets = {
            'book_title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ReadingLogForm, self).__init__(*args, **kwargs)
        # Ensure all fields have the 'form-control' class for consistent styling.
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control'
