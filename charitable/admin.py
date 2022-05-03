from django.contrib import admin
from .models import Cause, Document, EmailReminder, Organization, User, DonationRecord, VolunteerRecord, VolunteerGoal, DonationGoal, Profile

admin.site.register(User)
admin.site.register(DonationRecord)
admin.site.register(VolunteerRecord)
admin.site.register(VolunteerGoal)
admin.site.register(DonationGoal)
admin.site.register(Profile)
admin.site.register(EmailReminder)
admin.site.register(Document)
admin.site.register(Organization)
admin.site.register(Cause)