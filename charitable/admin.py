from django.contrib import admin
from .models import User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal

admin.site.register(User)
admin.site.register(Donationrecord)
admin.site.register(Volunteerrecord)
admin.site.register(Volunteergoal)
admin.site.register(Donationgoal)