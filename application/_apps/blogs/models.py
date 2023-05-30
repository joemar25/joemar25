from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=100, default="joemar25")
    category = models.CharField(max_length=50, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='blog/blog_img/thumbnails/', blank=True, null=True)
    images = models.ImageField(upload_to='blog/blog_img/images/', blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
