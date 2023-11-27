from .models import VolunteerProfile, Skills
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('user_name', 'fname', 'lname', 'phone', 'profile_picture', 'special_skills_description')
        
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('skills',)