from rest_framework.serializers import ModelSerializer
from .models import Company, Skill, Profile, Experience, Project, Followers


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullname', 'birthdate', 'Address', 'Phone', 'editor', 'github', 'linkedin', 'email', 'portfolio',
                  'job_type', 'account_type', 'level', 'skills', 'user']


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'logo', 'location', 'employees', 'admins']


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class FollowerSerializer(ModelSerializer):
    class Meta:
        model = Followers
        fields = ['follower', 'following']
