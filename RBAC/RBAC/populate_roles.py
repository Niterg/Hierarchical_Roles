from authentication.models import Role, Service, RolePermission
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RBAC.settings')
django.setup()


# Create Roles with hierarchy
roles = {
    "Admin": None,
    "A": "Admin",
    "B": "A"
}
role_objs = {}
for name, parent in roles.items():
    role_objs[name] = Role.objects.create(
        name=name, parent=role_objs.get(parent))

# Create Services
services = {name: Service.objects.create(name=name) for name in [
    "P", "Q", "R", "S"]}

# Define Role-Permission mapping
permissions = {
    "Admin": {"P": True, "Q": True, "R": True, "S": True},
    "A": {"Q": True, "R": False, "S": True},
    "B": {"S": False}
}

# Assign RolePermissions
for role, service_perms in permissions.items():
    for service, can_assign in service_perms.items():
        RolePermission.objects.create(
            role=role_objs[role],
            service=services[service],
            can_assign_roles=can_assign,
            can_use_service=True
        )

print("Roles, services, and permissions populated successfully!")
