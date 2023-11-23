from .models import VolunteerProfile
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('fname', 'lname', 'phone', 'profile_picture', 'special_skills_description')