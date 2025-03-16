from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import Service, UserProfile, AccessControl
from .forms import ServiceForm, AccessControlForm, UserCreationForm
from .serializers import AccessControlSerializer
from rest_framework import viewsets


def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('add_user')
    else:
        form = UserCreationForm()
    return render(request, 'access_control/add_user.html', {'form': form})


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_service')
    else:
        form = ServiceForm()
    return render(request, 'access_control/add_service.html', {'form': form})


def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
    else:
        form = ServiceForm()
    return render(request, 'create_service.html', {'form': form})


def assign_access(request, user_id):
    user = get_object_or_404(UserProfile, id=user_id)
    if request.method == 'POST':
        form = AccessControlForm(request.POST)
        if form.is_valid():
            access_control = form.save(commit=False)
            access_control.user = user
            access_control.save()
            return JsonResponse({'status': 'success'})
    else:
        form = AccessControlForm()
    return render(request, 'assign_access.html', {'form': form, 'user': user})


class AccessControlViewSet(viewsets.ModelViewSet):
    queryset = AccessControl.objects.all()
    serializer_class = AccessControlSerializer
