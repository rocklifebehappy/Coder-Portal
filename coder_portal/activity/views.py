from .models import (
    ProjectComment,
    ProjectReply,
    ProjectLike,
    BlogComment,
    BlogReply,
    BlogLike,
    Notification
)
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import (
    IsProjectCommenterOrReadOnly,
    IsProjectReplierOrReadOnly,
    IsBlogCommenterOrReadOnly,
    IsBlogReplierOrReadOnly,
    IsNotificationAuthorizedOrReadOnly)
from .serializers import (
    ProjectCommentSerializer,
    ProjectReplySerializer,
    ProjectLikeSerializer,
    BlogCommentSerializer,
    BlogReplySerializer,
    BlogLikeSerializer,
    NotificationSerializer
)


class ProjectCommentListView(ListCreateAPIView):
    serializer_class = ProjectCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectComment.objects.filter(project__id=self.kwargs.get('pk', None))


class ProjectCommentView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectCommentSerializer
    permission_classes = (IsProjectCommenterOrReadOnly,)
    queryset = ProjectComment.objects.all()


class ProjectReplyListView(ListCreateAPIView):
    serializer_class = ProjectReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectReply.objects.filter(comment__id=self.kwargs.get('pk', None))


class ProjectReplyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectReplySerializer
    permission_classes = (IsProjectReplierOrReadOnly,)
    queryset = ProjectReply.objects.all()


class ProjectLikeView(ListCreateAPIView):
    serializer_class = ProjectLikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return ProjectLike.objects.filter(project__id=self.kwargs.get('pk', None))


class BlogCommentListView(ListCreateAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogComment.objects.filter(blog__id=self.kwargs.get('pk', None))


class BlogCommentView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogCommentSerializer
    permission_classes = (IsBlogCommenterOrReadOnly,)
    queryset = BlogComment.objects.all()


class BlogReplyListView(ListCreateAPIView):
    serializer_class = BlogReplySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogReply.objects.filter(comment__id=self.kwargs.get('pk', None))


class BlogReplyView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlogReplySerializer
    permission_classes = (IsBlogReplierOrReadOnly,)
    queryset = BlogReply.objects.all()


class BlogLikeView(ListCreateAPIView):
    serializer_class = BlogLikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return BlogLike.objects.filter(blog__id=self.kwargs.get('pk', None))


class NotificationView(ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = (permissions.IsAuthenticated, IsNotificationAuthorizedOrReadOnly,)

    def get_queryset(self):
        return Notification.objects.filter(notification_to__id=self.kwargs.get('pk', None))
