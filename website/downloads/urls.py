from django.urls import path
from django.views.generic import ListView, DetailView
from downloads.models import Files

urlpatterns = [
    path('', ListView.as_view(queryset=Files.objects.all().order_by('Name'), template_name='downloads/files.html')),
]
