from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Blog
from rest_framework.response import Response
from rest_framework.decorators import api_view


class BlogListView(ListView):
    template_name = "blog/blogs.html"
    queryset = Blog.objects.all()


@api_view(['POST'])
def update_views(request):
    name = request.data["name"]

    blog = Blog.objects.get(slug=name)
    blog.views += 1
    blog.save()

    return Response({})


class BlogDetailView(DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Blog.objects.all()
