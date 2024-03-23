from django.urls import path
from django.views.generic import RedirectView

from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(url='/profile/')),

    path('<str:username>/notes/', note_list, name='note_list'),
    path('<str:username>/daily-book/', dailybook_list, name='dailybook_list'),
    path('<str:username>/daily-book/add/', DailybookCreateView.as_view(), name='dailybook_create'),
    path('<str:username>/daily-book/<int:pk>/', DailybookDetailView.as_view(), name='dailybook_detail'),
    path('<str:username>/daily-book/<int:pk>/edit/', DailybookUpdateView.as_view(), name='dailybook_edit'),
    path('<str:username>/note/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('<str:username>/note/add/', EntryCreateView.as_view(), name='entry_create'),
    path('<str:username>/note/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
    path('search/', search_results, name='search_results'),
    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
