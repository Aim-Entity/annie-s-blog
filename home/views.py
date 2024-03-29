from django.shortcuts import render
from blog_list.models import Blog
from .models import FavouriteBlog, News, TopBlog, AffiliateProduct
from blog_list.models import Blog


def index(request):
    blogs = Blog.objects.all()[:4]
    recentBlogs = Blog.objects.all()[:3]
    topBlog = TopBlog.objects.all()[:3]
    products = AffiliateProduct.objects.all()[:3]
    
    context = {
        "recent": recentBlogs,
        "top": topBlog,
        "blogs": blogs,
        "products": products
    }
    return render(request, "home/index.html", context)
