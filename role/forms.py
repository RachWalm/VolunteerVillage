from .models import Role
from django import forms


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ('role',)
