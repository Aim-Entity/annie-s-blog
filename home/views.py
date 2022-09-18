from django.shortcuts import render
from blog_list.models import Blog
from .models import FavouriteBlog, News, TopBlog
from blog_list.models import Blog


def index(request):
    blogs = Blog.objects.all()[:4]
    favouriteBlog = FavouriteBlog.objects.all()[:3]
    topBlog = TopBlog.objects.all()[:3]
    context = {
        "favourite": favouriteBlog,
        "top": topBlog,
        "blogs": blogs
    }
    return render(request, "home/index.html", context)
