from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class CustomUserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # ('id', 'username', 'first_name', 'last_name', 'email', 'type', 'password')