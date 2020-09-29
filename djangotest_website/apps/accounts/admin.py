from django.contrib import admin
from .models import userPersona, UserProfile, UserInterest
# Register your models here.
admin.site.register(userPersona)
admin.site.register(UserProfile)
admin.site.register(UserInterest)