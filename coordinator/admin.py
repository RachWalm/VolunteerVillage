from django.contrib import admin
from .models import CoordinatorProfile, CharityProfile, Feedback

# Register your models here.
admin.site.register(CoordinatorProfile)
admin.site.register(CharityProfile)
admin.site.register(Feedback)