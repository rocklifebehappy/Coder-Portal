from django.urls import path
from .views import (
    ProfileView, CompanyView, CompanyListView, SkillView, ExperienceListView, ExperienceView)


urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile_detail'),
    path('company/', CompanyListView.as_view(), name='companies_list'),
    path('company/<int:pk>/', CompanyView.as_view(), name='company_detail'),
    path('skill/', SkillView.as_view(), name="skill_list"),
    path('experience/', ExperienceListView.as_view(), name='experience_list'),
    path('experience/<int:pk>/', ExperienceView.as_view(), name='experience_detail'),
]


