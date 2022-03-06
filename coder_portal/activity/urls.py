from django.urls import path
from .views import (
    ProjectCommentListView,
    ProjectCommentView,
    ProjectReplyListView,
    ProjectReplyView,
    ProjectLikeView,
    BlogCommentListView,
    BlogCommentView,
    BlogReplyListView,
    BlogReplyView,
    BlogLikeView,
    NotificationView
)

urlpatterns = [
    path('project_comment/<int:pk>/', ProjectCommentListView.as_view(), name='project_comments'),
    path('project_comment/detail/<int:pk>', ProjectCommentView.as_view(), name='project_comment_detail'),
    path('project_reply/<int:pk>/', ProjectReplyListView.as_view(), name='project_replies'),
    path('project_reply/detail/<int:pk>/', ProjectReplyView.as_view(), name='project_reply_detail'),
    path('project_like/<int:pk>/', ProjectLikeView.as_view(), name='project_like'),
    path('blog_comment/<int:pk>/', BlogCommentListView.as_view(), name='blog_comments'),
    path('blog_comment/detail/<int:pk>', BlogCommentView.as_view(), name='blog_comment_detail'),
    path('blog_reply/<int:pk>/', BlogReplyListView.as_view(), name='blog_replies'),
    path('blog_reply/detail/<int:pk>/', BlogReplyView.as_view(), name='blog_reply_detail'),
    path('blog_like/<int:pk>/', BlogLikeView.as_view(), name='blog_like'),
    path('notification/list/<int:pk>', NotificationView.as_view(), name='notification')

]
