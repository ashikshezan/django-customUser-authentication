from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUserModel, Profile
from .forms import CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    add_form = CustomUserCreationForm
    list_display = ['username', 'age', 'country']


admin.site.register(CustomUserModel, CustomUserAdmin)
admin.site.register(Profile)
