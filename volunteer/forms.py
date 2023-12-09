from .models import VolunteerProfile, Skills, TimePeriod
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('user_name', 'fname', 'lname', 'phone', 'profile_picture', 'special_skills_description')
        widgets = {
            'user_name': forms.HiddenInput(),
        }

        
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('user_name', 'name', 'skilled',)
        widgets = {
            'user_name': forms.HiddenInput(),
            'name': forms.HiddenInput(),
        }
        
        
class TimeForm(forms.ModelForm):
    class Meta:
        model = TimePeriod
        fields = ('user_name', 'name', 'time_length_hours', 'time_length_days', 'section_of_day', 'day')
        widgets = {
            'user_name': forms.HiddenInput(),
            'name': forms.HiddenInput(),
        }