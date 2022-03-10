from rest_framework.serializers import ModelSerializer
from .models import (
    ProjectComment,
    ProjectLike,
    ProjectReply,
    BlogComment,
    BlogReply,
    BlogLike,
    Notification
)


class ProjectCommentSerializer(ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = '__all__'


class ProjectReplySerializer(ModelSerializer):
    class Meta:
        model = ProjectReply
        fields = '__all__'


class ProjectLikeSerializer(ModelSerializer):
    class Meta:
        model = ProjectLike
        fields = '__all__'


class BlogCommentSerializer(ModelSerializer):
    class Meta:
        model = BlogComment
        fields = '__all__'


class BlogReplySerializer(ModelSerializer):
    class Meta:
        model = BlogReply
        fields = '__all__'


class BlogLikeSerializer(ModelSerializer):
    class Meta:
        model = BlogLike
        fields = '__all__'


class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
