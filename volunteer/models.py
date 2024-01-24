from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class SkillChoices(models.Model):
    '''List of the skill choices model'''
    name= models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class VolunteerProfile(models.Model):
    """Personal information about the volunteer"""
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    # name = models.CharField(max_length=128)
    fname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='First Name',
        help_text='This is required and has a maximum length of 50 characters',
    )
    lname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Last Name',
        help_text='This is required and has a maximum length of 50 characters',
    )
    phone = models.CharField(
        max_length=12,
        blank=False,
        null=False,
        help_text='Must be 11 digits and numerical',
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    skilled = models.ManyToManyField(
        SkillChoices, 
        help_text='To select multiple activities hold control and click',
        verbose_name=("Activity options"),
        related_name="VolunteerProfiles")
    special_skills_description = models.TextField(
        null=False,
        blank=True,
        verbose_name='Information',
        max_length = 500,
        help_text='If you wish to provide us with specific information about skills - type it here',
    )
    activated = models.BooleanField(
        default=False,
    )
    time_length_hours = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Hours per week you can be available',
        validators=[
            MaxValueValidator(168), #168 hours in a week
        ])    
    time_length_days = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='days per week you can be available',
        validators=[
            MaxValueValidator(7), #7 days in a week
        ])
    mon_am = models.BooleanField(
        default=False,
        verbose_name="Monday morning",
    )
    mon_pm = models.BooleanField(
        default=False,
        verbose_name="Monday afternoon",
    )
    mon_ev = models.BooleanField(
        default=False,
        verbose_name="Monday evening",
    )
    tue_am = models.BooleanField(
        default=False,
        verbose_name="Tuesday morning",
    )
    tue_pm = models.BooleanField(
        default=False,
        verbose_name="Tuesday afternoon",
    )
    tue_ev = models.BooleanField(
        default=False,
        verbose_name="Tuesday Evening",
    )
    wed_am = models.BooleanField(
        default=False,
        verbose_name="Wednesday morning",
    )
    wed_pm = models.BooleanField(
        default=False,
        verbose_name="Wednesday afternoon",
    )
    wed_ev = models.BooleanField(
        default=False,
        verbose_name="Wednesday evening",
    )
    thu_am = models.BooleanField(
        default=False,
        verbose_name="Thursday morning",
    )
    thu_pm = models.BooleanField(
        default=False,
        verbose_name="Thursday afternoon",
    )
    thu_ev = models.BooleanField(
        default=False,
        verbose_name="Thursday Evening",
    )
    fri_am = models.BooleanField(
        default=False,
        verbose_name="Friday morning",
    )
    fri_pm = models.BooleanField(
        default=False,
        verbose_name="Friday afternoon",
    )
    fri_ev = models.BooleanField(
        default=False,
        verbose_name="Friday evening",
    )
    sat_am = models.BooleanField(
        default=False,
        verbose_name="Saturday morning",
    )
    sat_pm = models.BooleanField(
        default=False,
        verbose_name="Saturday afternoon",
    )
    sat_ev = models.BooleanField(
        default=False,
        verbose_name="Saturday evening",
    )
    sun_am = models.BooleanField(
        default=False,
        verbose_name="Sunday morning",
    )
    sun_pm = models.BooleanField(
        default=False,
        verbose_name="Sunday afternoon",
    )
    sun_ev = models.BooleanField(
        default=False,
        verbose_name="Sunday evening",
    )


def __str__(self):
    return self.name
    