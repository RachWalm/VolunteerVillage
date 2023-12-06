from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
# from select_multiple_field.codecs import SelectMultipleField
# from django import forms
from django.core.validators import MaxValueValidator

# Section of the days that they are available
PART_OF_DAY = (
    (0, 'None'),
    (1, 'Morning'),
    (2, 'Afternoon'),
    (3, 'Evening'),
)

# Which days they are available
DAYS_OF_WEEK = (
    (0, 'None'),
    (1, 'Monday'),
    (2, 'Tuesday'),
    (3, 'Wednesday'),
    (4, 'Thursday'),
    (5, 'Friday'),
    (6, 'Saturday'),
    (7, 'Sunday'),
)


class SkillChoices(models.Model):
    '''List of the skill choices model'''
    SKILL_CHOICES = (
        (1, 'ADMINISTRATION'),
        (2, 'COMPANIONSHIP'),
        (3, 'DIY'),
        (4, 'DRIVING'),
        (5, 'EVENTS'),
        (6, 'ENVIRONMENTAL'),
        (7, 'FUNDRAISING'),
        (8, 'GARDENING'),
        (9, 'READING'),
        (10, 'SHOPPING'),
        (11, 'TUTORING'),
    )


class TimePeriod(models.Model):
    '''How long the volunteer can spend and when the volunteer is available'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
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
    section_of_day = models.IntegerField(choices=PART_OF_DAY, default = 0)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default = 0)
    
    def __str__(self):
        return self.name
    
    # def get_time_length_hours(self):
    #     """Get the number of hours the volunteer can be available"""
    #     return [self.time_length_hours]
    
    # def get_time_length_hours(self):
    #     """Get the number of days the volunteer can be available"""
    #     return [self.time_length_days]
    
    # def get_section_of_day(self):
    #     """Get which parts of the day volunteer can be available"""
    #     return [self.section_of_day]
    
    # def get_day(self):
    #     """Get which day of the week the volunteer can be available"""
    #     return 2 #dict(DAYS_OF_WEEK) #[self.day]


class Skills(models.Model):
    '''Choose which type of volunteering they would like to do according to skills'''
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    skilled = models.IntegerField(choices=SkillChoices.SKILL_CHOICES,)   
    time_link = models.ManyToManyField(TimePeriod, through="VolunteerProfile")
    
    def __str__(self):
        return self.name
    
    # def get_skills(self):
    #     """Get the chosen categories of skills of the volunteer"""
    #     return self.skills.all()

        # multi_select = forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=forms.CheckboxSelectMultiple)
        
        # skills = SelectMultipleField(
        #     max_length=30,
        #     choices=SKILL_CHOICES             settings.AUTH_USER_MODEL        choices=SkillChoices.SKILL_CHOICES,
        #     )

class VolunteerProfile(models.Model):
    """Personal information about the volunteer"""
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    time_link = models.ForeignKey(TimePeriod, on_delete=models.CASCADE, null=True, blank=True)
    skills_link = models.ForeignKey(Skills, on_delete=models.CASCADE, null=True, blank=True)
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


