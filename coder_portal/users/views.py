from rest_framework import generics
from .serializers import (
    ProfileSerializer,
    CompanySerializer,
    SkillSerializer,
    ExperienceSerializer,
    FollowerSerializer,
    ProjectSerializer)
from .models import Profile, Company, Skill, Experience, Followers, Project
from .permissions import IsAdminOrReadOnly, IsExperienceAuthorOrReadOnly, IsProfileOwner
from rest_framework import permissions
from django.contrib.auth import get_user_model


User = get_user_model()


class ProfileView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.kwargs.get('pk', None))


class ProfileEditView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsProfileOwner,)
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
    permission_classes = (IsExperienceAuthorOrReadOnly,)

    def get_queryset(self):
        return Experience.objects.filter(user=Profile.objects.get(user=self.request.user))


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


class FollowerDeleteView(generics.DestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = ()

    def get_queryset(self):
        print(Followers.objects.filter(following=self.kwargs.get('pk', None), follower=self.request.user))
        return Followers.objects.filter(following=self.kwargs.get('pk', None), follower=self.request.user)


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

    def get_queryset(self):
        return Project.objects.filter(profile__user__id=self.kwargs.get('pk', None))


class ProjectView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Project.objects.all()
