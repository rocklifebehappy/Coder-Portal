from django.shortcuts import render
from .serializers import BlogFormSerializer
from rest_framework.views import APIView
from .models import Blog


class BlogViewSet(APIView):
    blogs = Blog.objects.all()
    serializer = BlogFormSerializer(blogs, many=True)
