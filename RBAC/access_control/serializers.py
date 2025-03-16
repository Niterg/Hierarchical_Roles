from rest_framework import serializers
from .models import AccessControl

class AccessControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessControl
        fields = '__all__'

# rbac/views.py
from rest_framework import viewsets
from .models import AccessControl
from .serializers import AccessControlSerializer

class AccessControlViewSet(viewsets.ModelViewSet):
    queryset = AccessControl.objects.all()
    serializer_class = AccessControlSerializer