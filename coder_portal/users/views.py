from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import (
    ProfileSerializer,
    CompanySerializer,
    SkillSerializer,
    ExperienceSerializer,
    FollowerSerializer,
    ProjectSerializer)
from .models import Profile, Company, Skill, Experience, Followers, Project
from .permissions import IsAdminOrReadOnly, IsExperienceAuthorOrReadOnly
from rest_framework import permissions


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAdminOrReadOnly,)


class SkillView(generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class ExperienceListView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = (IsExperienceAuthorOrReadOnly,)


class ExperienceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = (IsExperienceAuthorOrReadOnly,)


class FollowerListView(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return Followers.objects.filter(following=user_id)


class FollowerCreateView(generics.CreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Followers.objects.all()


class ProjectCreateView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Project.objects.all()


class ProjectListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        user_id = self.kwargs.get('pk', None)
        return Project.objects.filter(profile__user=user_id)


class ProjectView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Project.objects.all()
