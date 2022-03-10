from django.urls import path
from .views import (
    ProfileView,
    ProfileEditView,
    CompanyView,
    CompanyListView,
    SkillView,
    ExperienceListView,
    ExperienceView,
    FollowerListView,
    FollowerCreateView,
    FollowerDeleteView,
    ProjectCreateView,
    ProjectView,
    ProjectListView
)

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile_detail'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile_edit'),
    path('company/', CompanyListView.as_view(), name='companies_list'),
    path('company/<int:pk>/', CompanyView.as_view(), name='company_detail'),
    path('skill/', SkillView.as_view(), name="skill_list"),
    path('experience/', ExperienceListView.as_view(), name='experience_list'),
    path('experience/<int:pk>/', ExperienceView.as_view(), name='experience_detail'),
    path('followers/', FollowerCreateView.as_view(), name='create_follower'),
    path('followers/<int:pk>/', FollowerListView.as_view(), name='follower_list'),
    path('followers/delete/<int:pk>/', FollowerDeleteView.as_view(), name='follower_delete'),
    path('project/create/', ProjectCreateView.as_view(), name='create_project'),
    path('project/list/<int:pk>/', ProjectListView.as_view(), name='project_list'),
    path('project/detail/<int:pk>/', ProjectView.as_view(), name='project_detail')
]
