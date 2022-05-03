from django.contrib import admin
from .models import Document, EmailReminder, User, Record, Goal, Profile

admin.site.register(User)
admin.site.register(Record)
admin.site.register(Goal)
admin.site.register(Profile)
admin.site.register(EmailReminder)
admin.site.register(Document)
