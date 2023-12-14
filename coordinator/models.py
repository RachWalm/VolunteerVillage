from django.db import models
from django.contrib.auth.models import User

class CoordinatorProfile(models.Model):
    '''Details of the coordinator and link to which charities they are associated with'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
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
    coordinators_charities = models.ManyToManyField("coordinator.CharityProfile", verbose_name=("coordinators associated charities"))
    activated = models.BooleanField(
        default=False,
    )

    
class CharityProfile(models.Model):
    '''Details of the charity and link to which coordinators they are associated with'''
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
    charities_coordinators = models.ManyToManyField("coordinator.CoordinatorProfile", verbose_name=("coordinators associated with charity"))
    
class Feedback(models.Model):
    '''Details of the coordinator making the notes and volunteer they are associated with'''
    coordinator = models.ManyToManyField(
        "coordinator.CoordinatorProfile",
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