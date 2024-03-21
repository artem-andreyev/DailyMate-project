from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, FormView
from .models import Entry, Dailybook
from .forms import DailybookForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import Http404, HttpResponseForbidden


@login_required
def dailybook_list(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    dailybooks = Dailybook.objects.filter(author=user)
    return render(request, 'dailybook_list.html', {'dailybooks': dailybooks})


@login_required
def note_list(request, username):
    if request.user.username != username:
        return HttpResponseForbidden()
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        entries = Entry.objects.filter(author=user)
        return render(request, 'note_list.html', {'entries': entries})


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'note_detail.html'
    context_object_name = 'entry'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username != username:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class DailybookDetailView(LoginRequiredMixin, DetailView):
    model = Dailybook
    template_name = 'dailybook_detail.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username != username:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    template_name = 'note_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.username = self.kwargs['username']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('note_list', kwargs={'username': self.kwargs['username']})


class DailybookCreateView(LoginRequiredMixin, CreateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'dailybook_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.username = self.kwargs['username']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dailybook_list', kwargs={'username': self.kwargs['username']})


class DailybookUpdateView(LoginRequiredMixin, UpdateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'dailybook_form.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        entry = self.get_object()
        if request.user != entry.author or request.user.username != username:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('dailybook_list', kwargs={'username': self.kwargs['username']})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    template_name = 'note_form.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        entry = self.get_object()
        if request.user != entry.author or request.user.username != username:
            return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('note_list', kwargs={'username': self.kwargs['username']})


@login_required
def profile_view(request):
    return render(request, 'user/profile.html')


def log_out(request):
    return render(request, 'registration/logout.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
