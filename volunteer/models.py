from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from cloudinary.models import CloudinaryField
# from django_mysql.models import ListCharField
# from django.contrib.postgres.fields import ArrayField
# from phonenumber_field.modelfields import PhoneNumberField
# from select_multiple_field.codecs import SelectMultipleField
# from django import forms
from django.core.validators import MaxValueValidator

# # Section of the days that they are available
# PART_OF_DAY = (
#     (0, 'None'),
#     (1, 'Morning'),
#     (2, 'Afternoon'),
#     (3, 'Evening'),
# )

# # Which days they are available
# DAYS_OF_WEEK = (
#     (0, 'None'),
#     (1, 'Monday'),
#     (2, 'Tuesday'),
#     (3, 'Wednesday'),
#     (4, 'Thursday'),
#     (5, 'Friday'),
#     (6, 'Saturday'),
#     (7, 'Sunday'),
# )


class SkillChoices(models.Model):
    '''List of the skill choices model'''
    name= models.CharField(max_length=50)
    # profile = models.ManyToManyField("Skills", verbose_name=("users"), related_name=("SkillChoices"),)
    # makechoice_link = models.ForeignKey("volunteer.Skills", verbose_name=("skill"), on_delete=models.CASCADE,)
    # SKILL_CHOICES = (
    #     (1, 'ADMINISTRATION'),
    #     (2, 'COMPANIONSHIP'),
    #     (3, 'DIY'),
    #     (4, 'DRIVING'),
    #     (5, 'EVENTS'),
    #     (6, 'ENVIRONMENTAL'),
    #     (7, 'FUNDRAISING'),
    #     (8, 'GARDENING'),
    #     (9, 'READING'),
    #     (10, 'SHOPPING'),
    #     (11, 'TUTORING'),
    # )


    def __str__(self):
        return self.name


# class TimePeriod(models.Model):
#     '''How long the volunteer can spend and when the volunteer is available'''
#     user_name = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)
#     # timed = models.ManyToManyField("volunteer.Skills", verbose_name=("Time")) 
#     time_length_hours = models.PositiveSmallIntegerField(
#         default=0,
#         validators=[
#             MaxValueValidator(168), #168 hours in a week
#         ])    
#     time_length_days = models.PositiveSmallIntegerField(
#         default=0,
#         validators=[
#             MaxValueValidator(7), #7 days in a week
#         ])
#     mon_am = models.BooleanField(default=False, blank=True)
#     mon_pm = models.BooleanField(default=False, null=True, blank=True)
#     mon_ev = models.BooleanField(default=False, null=True, blank=True)
#     tue_am = models.BooleanField(default=False, null=True, blank=True)
#     tue_pm = models.BooleanField(default=False, null=True, blank=True)
#     tue_ev = models.BooleanField(default=False, null=True, blank=True)
#     wed_am = models.BooleanField(default=False, null=True, blank=True)
#     wed_pm = models.BooleanField(default=False, null=True, blank=True, verbose_name = "Wednesday Afternoon")
#     wed_ev = models.BooleanField(default=False, null=True, blank=True)
#     thu_am = models.BooleanField(default=False, null=True, blank=True)
#     thu_pm = models.BooleanField(default=False, null=True, blank=True)
#     thu_ev = models.BooleanField(default=False, null=True, blank=True)
#     fri_am = models.BooleanField(default=False, null=True, blank=True)
#     fri_pm = models.BooleanField(default=False, null=True, blank=True)
#     fri_ev = models.BooleanField(default=False, null=True, blank=True)
#     sat_am = models.BooleanField(default=False, null=True, blank=True)
#     sat_pm = models.BooleanField(default=False, null=True, blank=True)
#     sat_ev = models.BooleanField(default=False, null=True, blank=True)
#     sun_am = models.BooleanField(default=False, null=True, blank=True)
#     sun_pm = models.BooleanField(default=False, null=True, blank=True)
#     sun_ev = models.BooleanField(default=False, null=True, blank=True)
    
#         # section_of_day = models.IntegerField(choices=PART_OF_DAY, default = 0)
#     # day = models.IntegerField(choices=DAYS_OF_WEEK, default = 0)
    
#     def __str__(self):
#         return self.name
    
    
# class Skills(models.Model):
#     '''Choose which type of volunteering they would like to do according to skills'''
#     user_name = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)
#     skilled = models.ManyToManyField("SkillChoices", verbose_name=("skills"), related_name=("Skills"),) # choices= SkillChoices.objects.filter().values_list())   
#     # link = models.ForeignKey("volunteer.VolunteerProfile", verbose_name=("VProfile"), on_delete=models.CASCADE, null=True, blank=True) #I think this needs to be  a link to volunteer profile
    
#     def __str__(self):
#         return self.name
    

class VolunteerProfile(models.Model):
    """Personal information about the volunteer"""
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
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
        verbose_name="Sunday eveing",
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