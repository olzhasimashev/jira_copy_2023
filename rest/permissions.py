from rest_framework import permissions
    
class IsManagerUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_manager
    
class IsSelfUserOrReadOnly(permissions.BasePermission):
    # Custom permission to only allow users to edit their own profile
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj == request.user

class IsTaskExecutorOrReadOnly(permissions.BasePermission):
    # Custom permission to only allow executors of a task to update the task's is_active field
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the executors of the task
        if request.method in ['PUT', 'PATCH']:
            return request.user.is_authenticated and request.user.executor in obj.executors.all()

        return False