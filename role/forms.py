from .models import Role
from django import forms


class RoleForm(forms.ModelForm):
    '''Form to collect whether volunteer or coordinator'''
    class Meta:
        model = Role
        fields = ('role',)
