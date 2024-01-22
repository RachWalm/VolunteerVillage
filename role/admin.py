from django.contrib import admin
from .models import Role, RoleChoices


admin.site.register(Role)
admin.site.register(RoleChoices)
