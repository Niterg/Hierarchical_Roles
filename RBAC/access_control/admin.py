from django.contrib import admin
from .models import Service, UserProfile, AccessControl

admin.site.register(Service)
admin.site.register(UserProfile)
admin.site.register(AccessControl)
