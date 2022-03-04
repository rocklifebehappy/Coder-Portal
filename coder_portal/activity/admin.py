from django.contrib import admin
from .models import ProjectComment, ProjectReply, ProjectLike, BlogLike, BlogComment, BlogReply, Notification

admin.site.register(ProjectComment)
admin.site.register(ProjectReply)
admin.site.register(ProjectLike)
admin.site.register(BlogLike)
admin.site.register(BlogComment)
admin.site.register(BlogReply)
admin.site.register(Notification)
