from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'date_modified']

    widgets = {
        'date_modified': forms.DateInput(attrs={'type': 'datetime-local'}),
    }


class EntryUpdateForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content', 'date_modified']