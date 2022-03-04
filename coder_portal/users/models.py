from django.db import models
from django.contrib.auth.models import User

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time")
)

ACCOUNT_TYPE = (
    ("Talent", "Talent"),
    ("Recruiter", "Recruiter")
)

LEVEL = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Expert", "Expert")
)


class Company(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    logo = models.ImageField(upload_to="Company Logos")
    admins = models.ManyToManyField(User)
    location = models.CharField(max_length=60, blank=False, null=False)
    employees = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Companies"


class Skill(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    language = models.CharField(max_length=40, blank=False, null=False)
    description = models.TextField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=60, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    Address = models.CharField(max_length=60, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    editor = models.BooleanField(default=False)
    github = models.URLField(max_length=128, blank=True, null=True)
    linkedin = models.URLField(max_length=128, blank=True, null=True)
    email = models.URLField(max_length=128, blank=True, null=True)
    portfolio = models.URLField(max_length=128, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, null=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE, blank=True, null=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE, blank=True, null=True)
    level = models.CharField(max_length=20, choices=LEVEL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"


class Experience(models.Model):
    Designation = models.CharField(max_length=50, blank=False, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    date_left = models.DateField(blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.Designation

    class Meta:
        verbose_name_plural = "Experiences"


class Project(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="Project Thumbnails")
    Description = models.TextField(max_length=150, blank=True, null=True)
    github = models.URLField(max_length=128, blank=True, null=True)
    contributors = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_published = models.DateField(auto_now_add=True, auto_now=False)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"


class Followers(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.following

    class Meta:
        verbose_name_plural = "Followers"
