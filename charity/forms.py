from .models import CharityProfile
from django import forms


class CharityForm(forms.ModelForm):
    '''
    This form allows coordinators to add the details
    of a charity to the database and connect it to
    supervising coordinators.
    '''
    class Meta:
        model = CharityProfile
        fields = ('charity_name', 'charity_description',
                  'charities_coordinators')
