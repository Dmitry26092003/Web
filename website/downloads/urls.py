from django.urls import path
from django.views.generic import ListView, DetailView
from downloads.models import File

urlpatterns = [
    path('', ListView.as_view(queryset=File.objects.all().order_by('Name'), template_name='downloads/files.html')),
]
