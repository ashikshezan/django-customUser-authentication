from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class CustomUserModel(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=30)


class Profile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    team = models.CharField(max_length=20)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=CustomUserModel)
