from .models import VolunteerProfile, Skills, TimePeriod
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('fname', 'lname', 'phone', 'profile_picture', 'special_skills_description',)
        

        
class SkillsForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('skilled',)
        # widgets = {
        #     'user_name': initial= request.user,
        #     'name': forms.HiddenInput(),
        #     #'skilled': forms.SelectMultiple(),
        # }
        
        
class TimeForm(forms.ModelForm):
    class Meta:
        model = TimePeriod
        fields = ('time_length_hours', 'time_length_days', 'section_of_day', 'day',)
        # widgets = {
        #     'user_name': forms.HiddenInput(),
        #     'name': forms.HiddenInput(),
        # }