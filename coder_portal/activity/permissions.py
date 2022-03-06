from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsProjectCommenterOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsProjectReplierOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsBlogCommenterOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsBlogReplierOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.user == request.user


class IsNotificationAuthorizedOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        return view.kwargs.get('pk', None) == request.user.id
