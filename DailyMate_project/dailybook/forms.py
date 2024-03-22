from django import forms
from django.contrib.auth.forms import BaseUserCreationForm

from .models import Entry, Dailybook, UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Entry


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100, required=False)


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


class RegisterForm(BaseUserCreationForm):
    pass
