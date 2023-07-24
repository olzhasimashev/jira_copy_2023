from rest_framework import permissions

class IsExecutorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_executor
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_executor
    
class IsManagerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_manager