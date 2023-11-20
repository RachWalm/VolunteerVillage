from django.db import models
from django.contrib.auth.models import User

class CoordinatorProfile(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='First Name',
        help_text='format: required, max_length=50',
    )
    lname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Last Name',
        help_text='format: required, max_length=50',
    )
    coordinators_charities = models.ManyToManyField("self", verbose_name=("coordinators associated charities"))
    
    
class CharityProfile(models.Model):
    charity_name = models.CharField(
    max_length=50,
    null=False,
    blank=False,
    verbose_name='Charity Name',
    help_text='format: required, max_length=50',
    )
    charity_description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Charity Description',
    )
    charities_coordinators = models.ManyToManyField("Coordinator.CoordinatorProfile", verbose_name=("coordinators associated with charity"))
    
class Feedback(models.Model):
    coordinator = models.ManyToManyField(
        "Coordinator.CoordinatorProfile",
        verbose_name=("Coordinator"))
    volunteer = models.ManyToManyField(
        User,
        verbose_name=("Volunteer")
        )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now_add = True,
    )
    notes = models.TextField(
        null=False,
        verbose_name='Notes on activity',
    )