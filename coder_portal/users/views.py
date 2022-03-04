from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import ProfileSerializer, CompanySerializer, SkillSerializer, ExperienceSerializer, FollowersSerializer, ProjectSerializer
from .models import Profile, Company, Skill, Experience
from .permissions import IsAdminOrReadOnly, IsExperienceAuthorOrReadOnly
from rest_framework import permissions


class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class CompanyListView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class CompanyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAdminOrReadOnly, )


class SkillView(generics.ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class ExperienceListView(generics.ListCreateAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = (IsExperienceAuthorOrReadOnly, )


class ExperienceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes = (IsExperienceAuthorOrReadOnly, )
