from django import forms
from .models import Entry, Dailybook, UserProfile


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']


class DailybookForm(forms.ModelForm):
    class Meta:
        model = Dailybook
        fields = ['title', 'content', 'emotion', 'date_edit']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
