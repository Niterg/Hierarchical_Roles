from rest_framework.permissions import BasePermission
from .models import RolePermission


class CanAssignRole(BasePermission):
    """Check if the user can assign roles to others"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user_role = request.user.role
        return RolePermission.objects.filter(role=user_role, can_assign_roles=True).exists()


class CanUseService(BasePermission):
    """Check if the user has permission to use a service"""

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        service_id = view.kwargs.get('service_id')
        user_role = request.user.role
        return RolePermission.objects.filter(role=user_role, service_id=service_id, can_use_service=True).exists()
