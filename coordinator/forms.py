from .models import CoordinatorProfile, ChooseCoordinator
from django import forms

class ProfileFormCo(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname',)
        
class ProfileFormCoUpdate(forms.ModelForm):
    class Meta:
        model = CoordinatorProfile
        fields = ('fname', 'lname','activated')
        
# class ChooseCo(forms.ModelForm):
#     class Meta:
#         model = ChooseCoordinator
#         fields = ('first', 'last',)