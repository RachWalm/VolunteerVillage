from .models import VolunteerProfile
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('fname', 'lname', 'phone', 'skilled', 'special_skills_description', 'time_length_hours', 'time_length_days', 'mon_am', 'mon_pm', 'mon_ev', 'tue_am', 'tue_pm', 'tue_ev', 'wed_am', 'wed_pm', 'wed_ev', 'thu_am', 'thu_pm', 'thu_ev', 'fri_am', 'fri_pm', 'fri_ev', 'sat_am', 'sat_pm', 'sat_ev', 'sun_am', 'sun_pm', 'sun_ev',)
        

        
# class SkillsForm(forms.ModelForm):
#     class Meta:
#         model = Skills
#         fields = ('skilled',)
        
# class TimeForm(forms.ModelForm):
#     class Meta:
#         model = TimePeriod
#         fields = ('time_length_hours', 'time_length_days', 'mon_am', 'mon_pm', 'mon_ev', 'tue_am', 'tue_pm', 'tue_ev', 'wed_am', 'wed_pm', 'wed_ev', 'thu_am', 'thu_pm', 'thu_ev', 'fri_am', 'fri_pm', 'fri_ev', 'sat_am', 'sat_pm', 'sat_ev', 'sun_am', 'sun_pm', 'sun_ev',)