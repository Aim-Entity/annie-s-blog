from django.db import models


class Blog(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnail")
    image = models.ImageField(upload_to="blogs")
    title = models.CharField(max_length=300)
    thumbnail_text = models.CharField(max_length=1000)
    slug = models.SlugField()

    date = models.DateField(auto_now=True)
    views = models.IntegerField(default=0)

    par1 = models.CharField(max_length=30000)
    par2 = models.CharField(max_length=30000)

    image2 = models.ImageField(upload_to="blogs", null=True, blank=True)
    par3 = models.CharField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.title
