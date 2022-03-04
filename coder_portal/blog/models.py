from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    description = models.TextField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Blog(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    Thumbnail = models.ImageField(upload_to="Blog Thumbnails", blank=True, null=True)
    overview = models.TextField(max_length=150, blank=False, null=False)
    body_text = RichTextField(null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    date_published = models.DateField(auto_now_add=True, auto_now=False)
    date_modified = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blogs"
