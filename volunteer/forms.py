from .models import VolunteerProfile, Skills, TimePeriod
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('user_name', 'fname', 'lname', 'phone', 'profile_picture', 'special_skills_description')

        
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('user_name', 'skilled',)
        # widgets = {
        #     'skills': forms.Select(
        #         attrs={
        #             'class': 'form-control', 'required': True
        #         })
        # }
        
        
class TimeForm(forms.ModelForm):
    class Meta:
        model = TimePeriod
        fields = ('user_name', 'time_length_hours', 'time_length_days', 'section_of_day', 'day')