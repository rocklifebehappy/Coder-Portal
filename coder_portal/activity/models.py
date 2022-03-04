from django.db import models
from django.contrib.auth.models import User
from users.models import Project, Profile
from blog.models import Blog


class ProjectComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150, blank=False, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Project Comments"


class ProjectReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField(max_length=150, blank=False, null=False)
    comment = models.ForeignKey(ProjectComment, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now=False, auto_now_add=True)
    date_modified = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.reply

    class Meta:
        verbose_name_plural = "Project Replies"


class ProjectLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.project.name

    class Meta:
        verbose_name_plural = "Project Likes"


class BlogLike(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.name

    class Meta:
        verbose_name_plural = "Blog Likes"


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=100, blank=False, null=False)
    date_posted = models.DateField(auto_now_add=True, auto_now=False)
    date_modified = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name_plural = "Blog Comments"


class BlogReply(models.Model):
    comment = models.ForeignKey(BlogComment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.TextField(max_length=100)
    date_posted = models.DateField(auto_now_add=True, auto_now=False)
    date_modified = models.DateField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.reply

    class Meta:
        verbose_name_plural = "Blog Replies"


class Notification(models.Model):
    notification_to = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    notification = models.CharField(max_length=80)
    redirect_to = models.URLField(max_length=128, blank=True, null=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.notification
