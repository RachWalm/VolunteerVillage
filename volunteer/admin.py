from django.contrib import admin
from .models import VolunteerProfile, Skills, SkillChoices

# Register your models here.
admin.site.register(VolunteerProfile)
admin.site.register(Skills)
admin.site.register(SkillChoices)
