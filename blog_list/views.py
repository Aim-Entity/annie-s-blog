from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin
from .models import Blog
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse
from django.http import HttpResponse

from .models import Test, Comment
from .forms import CommentForm

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

def create(request):
    if request.method == "POST":
        user = request.POST.get('user', False)
        message = request.POST.get('message', False)
        slug = request.POST.get('slug', False)
        
        blog = Blog.objects.get(slug=slug)
        
        new_comment = Comment(user=user, comment=message, likes=0, blog=blog)
        new_comment.save()
        
        success = "Comment created successfully"
    
        return HttpResponse(success)
        # return render(request, "create/create.html")

class BlogDetailView(FormMixin, DetailView):
    template_name = "blog/blog_detail.html"
    queryset = Blog.objects.all()
    form_class = CommentForm
    
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(BlogDetailView, self).form_valid(form)
