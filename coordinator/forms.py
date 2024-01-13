from django import forms
from .models import CoordinatorProfile
from volunteer.models import VolunteerProfile

class ProfileFormCo(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname',)
        
class ProfileFormCoUpdate(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname','activated',)
        
class ProfileFormVolunteer(forms.ModelForm):
    class Meta:
        model = VolunteerProfile
        fields = ('activated',)