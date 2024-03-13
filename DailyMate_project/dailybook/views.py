from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Entry, Dailybook
from .forms import EntryForm, DailybookForm
from django.urls import reverse_lazy


class EntryListView(ListView):
    model = Entry
    template_name = 'note_list.html'


class DailybookListView(ListView):
    model = Dailybook
    template_name = 'dailybook_list.html'


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'note_detail.html'


class DailybookDetailView(DetailView):
    model = Dailybook
    template_name = 'dailybook_detail.html'


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')


class DailybookCreateView(CreateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'dailybook_form.html'
    success_url = reverse_lazy('dailybook_list')


class DailybookUpdateView(UpdateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'dailybook_form.html'
    success_url = reverse_lazy('dailybook_list')


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note_list')
