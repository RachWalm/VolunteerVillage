from django import forms
from .models import CoordinatorProfile
from volunteer.models import VolunteerProfile


class ProfileFormCo(forms.ModelForm):
    ''' Form for coordinator to set up profile'''
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname',)


class ProfileFormCoUpdate(forms.ModelForm):
    '''
    Form for coordinator to change or activate
    another coordinator
    '''
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname', 'activated',)


class ProfileFormVolunteer(forms.ModelForm):
    '''Form for coordinator to activate volunteer'''
    class Meta:
        model = VolunteerProfile
        fields = ('activated',)
