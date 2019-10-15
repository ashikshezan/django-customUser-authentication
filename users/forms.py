from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUserModel


class CustomUserCreationForm(UserCreationForm):
    # age = forms.CharField()
    # country = forms.CharField()

    class Meta:
        model = CustomUserModel
        fields = ['username', 'age', 'country', 'first_name']
