from .models import (
    ProjectComment,
    ProjectReply,
    ProjectLike,
    BlogComment,
    BlogReply,
    BlogLike,
    Notification
)
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsProjectCommenterOrReadOnly, IsProjectReplierOrReadOnly, IsBlogCommenterOrReadOnly, IsBlogReplierOrReadOnly, IsNotificationAuthorizedOrReadOnly
from .serializers import (
    ProjectCommentSerializer,
    ProjectReplySerializer,
    ProjectLikeSerializer,
    BlogCommentSerializer,
    BlogReplySerializer,
    BlogLikeSerializer,
    NotificationSerializer
)


class ProjectCommentListView(generics.ListCreateAPIView):
    serializer_class = ProjectCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectComment.objects.filter(project__id=self.kwargs.get('pk', None))


class ProjectCommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectCommentSerializer
    permission_classes = (IsProjectCommenterOrReadOnly,)
    queryset = ProjectComment.objects.all()


class ProjectReplyListView(generics.ListCreateAPIView):
    serializer_class = ProjectReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectReply.objects.filter(comment__id=self.kwargs.get('pk', None))


class ProjectReplyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectReplySerializer
    permission_classes = (IsProjectReplierOrReadOnly,)
    queryset = ProjectReply.objects.all()


class ProjectLikeView(generics.ListCreateAPIView):
    serializer_class = ProjectLikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectLike.objects.filter(project__id=self.kwargs.get('pk', None))


class BlogCommentListView(generics.ListCreateAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogComment.objects.filter(blog__id=self.kwargs.get('pk', None))


class BlogCommentView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = (IsBlogCommenterOrReadOnly,)
    queryset = BlogComment.objects.all()


class BlogReplyListView(generics.ListCreateAPIView):
    serializer_class = BlogReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogReply.objects.filter(comment__id=self.kwargs.get('pk', None))


class BlogReplyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogReplySerializer
    permission_classes = (IsBlogReplierOrReadOnly,)
    queryset = BlogReply.objects.all()


class BlogLikeView(generics.ListCreateAPIView):
    serializer_class = BlogLikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogLike.objects.filter(blog__id=self.kwargs.get('pk', None))


class NotificationView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated, IsNotificationAuthorizedOrReadOnly,)

    def get_queryset(self):
        return Notification.objects.filter(notification_to__id=self.kwargs.get('pk', None))
