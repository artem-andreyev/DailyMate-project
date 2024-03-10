from django.views.generic import ListView, DetailView, CreateView
from .models import Entry
from django.urls import reverse_lazy

class EntryListView(ListView):
    model = Entry
    template_name = 'entry_list.html'

class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'

class EntryCreateView(CreateView):
    model = Entry
    template_name = 'entry_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('entry_list')
