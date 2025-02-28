from rest_framework import serializers
from .models import Role, Service, RolePermission, CustomUser

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"

class RolePermissionSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    service = ServiceSerializer()

    class Meta:
        model = RolePermission
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = CustomUser
        fields = ["id", "username", "role"]
