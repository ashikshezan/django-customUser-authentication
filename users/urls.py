from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [

    path('', user_views.UserHomeView.as_view(), name='home'),
    path('login/',
         auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('signup/',
         user_views.CreateUser.as_view(), name='signup'),

    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),
    path('update/<pk>/',
         user_views.UpdateUser.as_view(), name='update'),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
