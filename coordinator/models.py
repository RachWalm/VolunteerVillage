from django.db import models
from django.contrib.auth.models import User


class CoordinatorProfile(models.Model):
    '''Details of the coordinator'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='First Name',
        help_text='required, max length 50 characters',
    )
    lname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Last Name',
        help_text='required, max length 50 characters',
    )
    activated = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return str(self.fname + " " + self.lname)
