from rest_framework import permissions
  

class IsCurrentUserOwnerOrAdminOrReadOnlyForUser(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id or request.user.is_staff
  
class IsCurrentUserOwnerOrAdminOrReadOnlyForProfile(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user or request.user.is_staff