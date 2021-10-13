from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Blog


class BlogListView(ListView):
    template_name = "blog/blogs.html"
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Blog.objects.all()
