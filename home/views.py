from django.shortcuts import render
from blog_list.models import Blog


def index(request):
    context = {

    }
    return render(request, "home/index.html", context)
