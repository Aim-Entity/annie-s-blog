from django.db import models
from blog_list.models import Blog


class News(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "news"


class FavouriteBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} | {self.blog.date}"


class TopBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} | {self.blog.date}"
