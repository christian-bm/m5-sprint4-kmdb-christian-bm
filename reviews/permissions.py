from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


class IsOwnerReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
