from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', note_list, name='note_list'),
    path('daily-book/', dailybook_list, name='dailybook_list'),

    path('daily-book/add/', DailybookCreateView.as_view(), name='dailybook_create'),
    path('daily-book/<int:pk>/', DailybookDetailView.as_view(), name='dailybook_detail'),
    path('daily-book/<int:pk>/edit/', DailybookUpdateView.as_view(), name='dailybook_edit'),

    path('note/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('note/add/', EntryCreateView.as_view(), name='entry_create'),
    path('note/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),

    path('profile/', profile_view, name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
