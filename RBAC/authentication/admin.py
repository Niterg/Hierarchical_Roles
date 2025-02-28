from django.contrib import admin
from .models import Role, Service, RolePermission

admin.site.register(Role)
admin.site.register(Service)
admin.site.register(RolePermission)
