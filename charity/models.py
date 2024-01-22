from django.db import models
from coordinator.models import CoordinatorProfile


class CharityProfile(models.Model):
    '''Details of the charity and link to which coordinators they are associated with'''
    charity_name = models.CharField(
    max_length=50,
    null=False,
    blank=False,
    verbose_name='Charity Name',
    help_text='required, max length 50 characters',
    )
    charity_description = models.TextField(
        null=False,
        blank=False,
        verbose_name='Charity Description',
    )
    charities_coordinators = models.ManyToManyField(
        CoordinatorProfile, 
        verbose_name=('coordinators associated with charity'),
        related_name='CharityProfiles',
        help_text='Hold control and click to select multiple',
        )
    
    
    def __str__(self):
        return self.charity_name