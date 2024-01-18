from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from cloudinary.models import CloudinaryField
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
        help_text='format: required, max_length=50',
    )
    lname = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Last Name',
        help_text='format: required, max_length=50',
    )
    phone = models.CharField(
        max_length=12,
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now_add = True,
    )
    # profile_picture = CloudinaryField(
    #     'image', default='placeholder',
    # )
    skilled = models.ManyToManyField(
        SkillChoices, 
        verbose_name=("Activity options"),
        related_name="VolunteerProfiles")
    special_skills_description = models.TextField(
        null=False,
        blank=True,
        verbose_name='special skills description',
        max_length = 500,
    )
    activated = models.BooleanField(
        default=False,
    )
    time_length_hours = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(168), #168 hours in a week
        ])    
    time_length_days = models.PositiveSmallIntegerField(
        default=0,
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
    
    '''def get_fname(self):
        """Get the first name of the volunteer"""
        return [self.fname]
    
    def get_lname(self):
        """Get the last name of the volunteer"""
        return [self.lname]
    
    def get_phone(self):
        """Get the phone number of the volunteer"""
        return [self.phone]
    
    def get_created_on(self):
        """Get the date the volunteer created the profile"""
        return [self.created_on]
    
    def get_updated_on(self):
        """Get the date the profile was last updated"""
        return [self.updated_on]
    
    def get_profile_picture(self):
        """Get the profile picture of the volunteer"""
        return [self.profile_picture]
    
    def get_special_skills_description(self):
        """Get the information provided by volunteer of special skills"""
        return [self.special_skills_description]'''