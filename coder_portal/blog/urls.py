from django.urls import path
from .views import BlogListView, BlogView, UsersBlogListView, CategoryView, CategoryListView

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name="blogs"),
    path('blogs/<int:pk>/', UsersBlogListView.as_view(), name='user_blogs'),
    path('blogs/detail/<int:pk>', BlogView.as_view(), name='blog_detail'),
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/<str:list>/', CategoryView.as_view(), name='category')
]