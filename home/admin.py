from django.contrib import admin
from .models import FavouriteBlog, News, TopBlog

admin.site.register(FavouriteBlog)
admin.site.register(TopBlog)
admin.site.register(News)
