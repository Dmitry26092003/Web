from django.urls import path
from django.views.generic import ListView, DetailView
from news.models import Post
from django.conf.urls import url


urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by('Name'), template_name='news/news.html')),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Post, template_name='news/post.html'))
]
