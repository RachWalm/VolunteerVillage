from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
# from select_multiple_field.codecs import SelectMultipleField
# from django import forms
from django.core.validators import MaxValueValidator



class VolunteerProfile(models.Model):
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
    phone = PhoneNumberField(
        max_length=11,
        blank=False,
        null=False,
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now_add = True,
    )
    profile_picture = CloudinaryField(
        'image', default='placeholder',
    )
    special_skills_description = models.TextField(
        null=False,
        blank=True,
        verbose_name='special skills description',
    )
    activated = models.BooleanField(
        default=False,
    )
    
class Skills(models.Model):
        user_name = models.ForeignKey(User, on_delete=models.CASCADE)
        class SkillChoices():
            skill_dict = {
                'AD': 'ADMINISTRATION',
                'CO': 'COMPANIONSHIP',
                'DI': 'DIY',
                'DR': 'DRIVING',
                'EV': 'EVENTS',
                'EN': 'ENVIRONMENTAL',
                'FU': 'FUNDRAISING',
                'GA': 'GARDENING',
                'RE': 'READING',
                'SH': 'SHOPPING',
                'TU': 'TUTORING',
            }
        
        skills = models.ManyToManyField('self')

        # multi_select = forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=forms.CheckboxSelectMultiple)
        
        # skills = SelectMultipleField(
        #     max_length=30,
        #     choices=SKILL_CHOICES
        #     )

    
class TimePeriod(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE),
    time_length_hours = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(168), #168 hours in a week
        ]),
    time_length_days = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(7), #7 days in a week
        ]),
    class TimeSlots(models.Model): # First three letters of day then AM/PM or EV for evening
        slot_dict = {
            'MONAM': models.BooleanField(default=False),
            'MONPM': models.BooleanField(default=False),
            'MONEV': models.BooleanField(default=False),
            'TUEAM': models.BooleanField(default=False),
            'TUEPM': models.BooleanField(default=False),
            'TUEEV': models.BooleanField(default=False),
            'WEDAM': models.BooleanField(default=False),
            'WEDPM': models.BooleanField(default=False),
            'WEDEV': models.BooleanField(default=False),
            'THUAM': models.BooleanField(default=False),
            'THUPM': models.BooleanField(default=False),
            'THUEV': models.BooleanField(default=False),
            'FRIAM': models.BooleanField(default=False),
            'FRIPM': models.BooleanField(default=False),
            'FRIEV': models.BooleanField(default=False),
            'SATAM': models.BooleanField(default=False),
            'SATPM': models.BooleanField(default=False),
            'SATEV': models.BooleanField(default=False),
            'SUNAM': models.BooleanField(default=False),
            'SUNPM': models.BooleanField(default=False),
            'SUNEV': models.BooleanField(default=False),
        }
        
    slots = models.ManyToManyField('self')