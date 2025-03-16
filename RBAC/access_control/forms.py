from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Service, AccessControl, UserProfile
from django.contrib.auth.models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Use the User model, not UserProfile
        fields = ['username', 'password1', 'password2']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description']


class AccessControlForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=UserProfile.objects.all(), widget=forms.CheckboxSelectMultiple)
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = AccessControl
        fields = ['users', 'services', 'can_access']
