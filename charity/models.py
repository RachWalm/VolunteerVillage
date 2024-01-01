from django.db import models
from django.contrib.auth.models import User


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
    
    def __str__(self):
        return self.charity_name