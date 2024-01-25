from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser

class IsPledgeContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user

class IsNothAuthenticatedReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view):
        return not request.user or request.user.is_anonymous
    
    def has_object_permission(self, request, view, obj):
        return not request.user or request.user.is_anonymous