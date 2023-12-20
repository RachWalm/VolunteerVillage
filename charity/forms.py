from .models import CharityProfile
from django import forms

class CharityForm(forms.ModelForm):
    class Meta:
        model = CharityProfile
        fields = ('charity_name', 'charity_description', 'charities_coordinators')