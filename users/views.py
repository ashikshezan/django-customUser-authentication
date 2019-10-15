from django.shortcuts import render
from django.views import generic
from .models import CustomUserModel
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class UserHomeView(generic.TemplateView):
    template_name = 'home.html'


class UpdateUser(generic.UpdateView):
    template_name = 'update.html'
    model = CustomUserModel
    success_url = reverse_lazy('home')
    fields = ['username', 'email', 'age', 'country']


class CreateUser(generic.CreateView):
    template_name = 'create.html'
    model = CustomUserModel
    success_url = reverse_lazy('home')
    form_class = CustomUserCreationForm


class HomeView(generic.TemplateView):
    template_name = 'login.html'
