from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Entry
from .forms import EntryForm
from django.urls import reverse_lazy

class EntryListView(ListView):
    model = Entry
    template_name = 'entry_list.html'

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'

class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entry_form.html'
    success_url = reverse_lazy('entry_list')

class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entry_form.html'
    success_url = reverse_lazy('entry_list')

