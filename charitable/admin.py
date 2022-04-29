from django.contrib import admin
from .models import Document, Emailreminder, User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal, Profile

admin.site.register(User)
admin.site.register(Donationrecord)
admin.site.register(Volunteerrecord)
admin.site.register(Volunteergoal)
admin.site.register(Donationgoal)
admin.site.register(Profile)
admin.site.register(Emailreminder)
admin.site.register(Document)