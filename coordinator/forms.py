from .models import CoordinatorProfile
from django import forms

class ProfileFormCo(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname',)