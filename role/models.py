from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class RoleChoices(models.Model):
    '''List of the role choices model'''
    ROLE_CHOICES = (
        (1, 'Volunteer'),
        (2, 'Coordinator'),
    )


class Role(models.Model):
    '''Which role and functions the user has'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=128)
    role = models.IntegerField(choices=RoleChoices.ROLE_CHOICES, default = 1)
    
    def __str__(self):
        return self.role
    