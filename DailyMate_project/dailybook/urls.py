from django.urls import path
from .views import EntryListView, EntryDetailView, EntryCreateView, EntryUpdateView

urlpatterns = [
    path('', EntryListView.as_view(), name='entry_list'),
    path('entry/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/add/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/<int:pk>/edit/', EntryUpdateView.as_view(), name='entry_edit'),
]
