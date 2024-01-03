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
    coordinators_charities = models.ManyToManyField("charity.CharityProfile", 
                                                    verbose_name=("coordinators associated charities"),
                                                    related_name="CoordinatorProfiles")
    activated = models.BooleanField(
        default=False,
    )
    
    def __str__(self):
        return str(self.fname + " " + self.lname)


class ChooseCoordinator(models.Model):  #probably don't need this model, but will delete when sure
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    
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