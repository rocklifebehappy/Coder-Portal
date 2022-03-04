from django.urls import path
from .views import BlogViewSet

urlpatterns = [
    path('', BlogViewSet.as_view(), name="blogs")
]