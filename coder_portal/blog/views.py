import ast
from .serializers import BlogSerializer, CategorySerializer
from .models import Blog, Category
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly


class BlogListView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UsersBlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return Blog.objects.filter(author=user_id)


class BlogView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Blog.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        pk = ast.literal_eval(self.kwargs.get('list', None))
        return Category.objects.filter(id__in=pk)
