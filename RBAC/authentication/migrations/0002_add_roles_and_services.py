# Generated by Django 5.1.6 on 2025-02-28 17:06
from django.db import migrations


def create_roles_and_services(apps, schema_editor):
    Role = apps.get_model('RBAC', 'Role')
    Service = apps.get_model('RBAC', 'Service')
    RolePermission = apps.get_model('RBAC', 'RolePermission')

    # Create Services
    services = {name: Service.objects.create(name=name) for name in [
        "P", "Q", "R", "S", "T", "U"]}

    # Create Roles
    admin_role = Role.objects.create(name="Admin")
    role_a = Role.objects.create(name="A", parent=admin_role)
    role_b = Role.objects.create(name="B", parent=role_a)

    # Define RolePermissions for Admin
    admin_permissions = [
        (admin_role, "P", True, True),
        (admin_role, "Q", True, True),
        (admin_role, "R", True, True),
        (admin_role, "S", True, True),
    ]

    # Define RolePermissions for Role A
    role_a_permissions = [
        (role_a, "Q", True, True),
        (role_a, "R", False, True),
        (role_a, "S", True, True),
    ]

    # Define RolePermissions for Role B
    role_b_permissions = [
        (role_b, "S", False, True),
    ]

    # Assign RolePermissions
    for role, service_name, can_assign, can_use in admin_permissions:
        RolePermission.objects.create(
            role=role, service=services[service_name], can_assign_roles=can_assign, can_use_service=can_use
        )

    for role, service_name, can_assign, can_use in role_a_permissions:
        RolePermission.objects.create(
            role=role, service=services[service_name], can_assign_roles=can_assign, can_use_service=can_use
        )

    for role, service_name, can_assign, can_use in role_b_permissions:
        RolePermission.objects.create(
            role=role, service=services[service_name], can_assign_roles=can_assign, can_use_service=can_use
        )


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_roles_and_services),
    ]
