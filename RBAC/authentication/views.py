from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Role, Service, RolePermission, CustomUser
from .serializers import RoleSerializer, ServiceSerializer, UserSerializer
from .permissions import CanAssignRole, CanUseService


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    # Only superusers can create roles
    permission_classes = [permissions.IsAdminUser]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["GET"], permission_classes=[CanUseService])
    def access(self, request, pk=None):
        service = self.get_object()
        return Response({"message": f"Access granted to {service.name}"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=["POST"], permission_classes=[CanAssignRole])
    def assign_role(self, request, pk=None):
        user = self.get_object()
        new_role_id = request.data.get("role_id")

        if not Role.objects.filter(id=new_role_id).exists():
            return Response({"error": "Invalid role ID"}, status=400)

        new_role = Role.objects.get(id=new_role_id)
        if user.role.parent == request.user.role or request.user.role.name == "Admin":
            user.role = new_role
            user.save()
            return Response({"message": f"Role {new_role.name} assigned to {user.username}"})
        else:
            return Response({"error": "You don't have permission to assign this role"}, status=403)
