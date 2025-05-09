from django import forms
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['picture', 'phone_number', 'street', 'city', 'zip_code']