from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogListView.as_view(), name="blog"),
    path("blog-detail", views.BlogListView.as_view(), name="blog-detail"),
    path("item/<str:slug>", views.BlogDetailView.as_view(), name="blog-detail"),
    path("update_views/", views.update_views)
]
