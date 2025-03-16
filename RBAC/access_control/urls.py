from rest_framework.routers import DefaultRouter
from .views import AccessControlViewSet
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register(r'access', AccessControlViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create_service/', views.create_service, name='create_service'),
    path('assign_access/<int:user_id>/',
         views.assign_access, name='assign_access'),
    path('add_user/', views.add_user, name='add_user'),
    path('add_service/', views.add_service, name='add_service'),
]

urlpatterns += router.urls
