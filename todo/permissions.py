from rest_framework.permissions import BasePermission, IsAdminUser

class IsStaffOrReadOnly(BasePermission):
    # This class that allows read-only access to staff members and denies access for other methods.
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user and request.user.is_staff:
            return True
        return False
    

class IsSuperUserOrReadOnly(BasePermission):
    #  class that allows read-only access to superusers (staff or admin) and denies access for other methods.
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        return False