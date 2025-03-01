from django import forms
from .models import Activity
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'duration', 'distance', 'calories_burned']


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

