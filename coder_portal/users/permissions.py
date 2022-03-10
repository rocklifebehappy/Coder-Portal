from rest_framework import permissions
from .models import Profile


class IsProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            profile = Profile.objects.get(user=request.user.id)
        except Profile.DoesNotExist:
            return False
        return view.kwargs.get('pk', None) == profile.id


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user in obj.admins.all()


class IsExperienceAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == Profile.objects.get(user=request.user)


class IsProjectAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
