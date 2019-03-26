from django.urls import path
from django.views.generic import ListView, DetailView
from downloads.models import File
from django.conf.urls import url

urlpatterns = [
    path('', ListView.as_view(queryset=File.objects.all().order_by('Name'), template_name='downloads/files.html')),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=File, template_name='downloads/file.html'))
]
