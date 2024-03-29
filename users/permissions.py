from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.user.is_superuser
        )

class IsAdminOrReadyOnly(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            # request.user and
            request.user.is_superuser
        )

class IsAdminOrCritic(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_superuser or
            obj.critic == request.user
        )
        