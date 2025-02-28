from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL)  # Hierarchical Roles

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # Add custom fields here if needed
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Add a custom related name to avoid conflicts
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        # Add a custom related name to avoid conflicts
        related_name='customuser_permissions_set',
        blank=True
    )


class Service(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    can_assign_roles = models.BooleanField(
        default=False)  # Can assign roles to others
    can_use_service = models.BooleanField(default=False)  # Can use the service

    def __str__(self):
        return f"{self.role.name} → {self.service.name} (Assign: {self.can_assign_roles}, Use: {self.can_use_service})"
