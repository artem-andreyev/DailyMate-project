from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, FormView
from .models import Entry, Dailybook
from .forms import DailybookForm, RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import Http404, HttpResponseForbidden

from .forms import SearchForm
from django.db.models import Q

from django.db.models import Q

@login_required
def search_results(request):
    query = request.GET.get('q')
    if query:
        entry_results = Entry.objects.filter(title__icontains=query, author=request.user)
        dailybook_results = Dailybook.objects.filter(title__icontains=query, author=request.user)
    else:
        entry_results = []
        dailybook_results = []
    return render(request, 'search_results.html', {'query': query, 'entry_results': entry_results, 'dailybook_results': dailybook_results})

@login_required
def dailybook_list(request, username):
    if request.user.username != username:
        return render(request, 'error/access_denied.html', status=403)
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        dailybooks = Dailybook.objects.filter(author=user)
        return render(request, 'main/dailybook_list.html', {'dailybooks': dailybooks})


@login_required
def note_list(request, username):
    print(request.user.username, username)
    if request.user.username != username:
        return render(request, 'error/access_denied.html', status=403)

        # return HttpResponseForbidden()
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404("User does not exist")

        entries = Entry.objects.filter(author=user)
        return render(request, 'main/note_list.html', {'entries': entries})


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry
    template_name = 'main/note_detail.html'
    context_object_name = 'entry'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username != username:
            return render(request, 'error/access_denied.html', status=403)
        return super().dispatch(request, *args, **kwargs)


class DailybookDetailView(LoginRequiredMixin, DetailView):
    model = Dailybook
    template_name = 'main/dailybook_detail.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        if request.user.username != username:
            # return HttpResponseForbidden()
            return render(request, 'error/access_denied.html', status=403)

        return super().dispatch(request, *args, **kwargs)


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    template_name = 'main/note_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.username = self.kwargs['username']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main/note_list', kwargs={'username': self.kwargs['username']})


class DailybookCreateView(LoginRequiredMixin, CreateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'main/dailybook_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.username = self.kwargs['username']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main/dailybook_list', kwargs={'username': self.kwargs['username']})


class DailybookUpdateView(LoginRequiredMixin, UpdateView):
    model = Dailybook
    form_class = DailybookForm
    template_name = 'main/dailybook_form.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        entry = self.get_object()
        if request.user != entry.author or request.user.username != username:
            return render(request, 'error/access_denied.html', status=403)
            # return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('dailybook_list', kwargs={'username': self.kwargs['username']})


class EntryUpdateView(LoginRequiredMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    template_name = 'main/note_form.html'

    def dispatch(self, request, *args, **kwargs):
        username = kwargs.get('username')
        entry = self.get_object()
        if request.user != entry.author or request.user.username != username:
            return render(request, 'error/access_denied.html', status=403)
            # return HttpResponseForbidden()
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('note_list', kwargs={'username': self.kwargs['username']})


@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')


def log_out(request):
    return render(request, 'registration/logout.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def page_not_found(request, exception):
    return render(request, 'error/page_not_found.html', status=404)
