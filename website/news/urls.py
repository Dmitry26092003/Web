from django.urls import path
from django.views.generic import ListView, DetailView
from news.models import Post

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by('Name'), template_name='news/news.html')),
]
