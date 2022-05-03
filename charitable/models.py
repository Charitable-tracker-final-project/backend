from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from charitable_tracker.storage_backends import PrivateMediaStorage
from charitable_tracker import settings
from django.core.mail import send_mail
from .tasks import mail_create

class User(AbstractUser):
    
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_profile")
    annual_income = models.IntegerField(null=True, blank=True)
    profile_pic = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return f"Annual Income {str(self.annual_income)}"

class DonationGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "donor")
    goaltitle = models.CharField(max_length=100, blank=True)
    donationgoal = models.IntegerField()
    created_at = models.DateField(default=datetime.now)

    #intervaldropdownlist
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    INTERVAL_DROPDOWN_CHOICES = [(WEEK,"Week"),(MONTH, "Month"), (YEAR, "Year")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL_DROPDOWN_CHOICES)

    def __str__(self):
        return self.goaltitle

class VolunteerGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "volunteer")
    goaltitle = models.CharField(max_length=100, blank=True)
    volunteergoal = models.IntegerField()
    created_at = models.DateField(default=datetime.now)

    #intervaldropdownlist
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    INTERVAL_DROPDOWN_CHOICES = [(WEEK,"Week"),(MONTH, "Month"), (YEAR, "Year")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL_DROPDOWN_CHOICES)

    def __str__(self):
        return self.goaltitle

class Organization(models.Model):
    organization = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "ouser", blank=True, null=True)
    donationgoal = models.ForeignKey(DonationGoal, on_delete=models.CASCADE, related_name = "donationgoalorg", blank=True, null=True)
    volunteergoal = models.ForeignKey(VolunteerGoal, on_delete=models.CASCADE, related_name = "volunteergoalorg", blank=True, null=True)

    def __str__(self):
        return self.organization


class Cause(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "cuser", blank=True, null=True)
    donationgoal = models.ForeignKey(DonationGoal, on_delete=models.CASCADE, related_name = "donationgoalcause", blank=True, null=True)
    volunteergoal = models.ForeignKey(VolunteerGoal, on_delete=models.CASCADE, related_name = "volunteergoalcause", blank=True, null=True)

    #causedropdownlist
    ANIMALS = "Animals"
    ARTS_CULTURE_HUMANITIES = "Arts Culture Humanities"
    ASIAN_RIGHTS = "Asian Rights"
    BLACK_RIGHTS = "Black Rights"
    COMMUNITY_DEVELOPMENT = "Community Development"
    EDUCATION = "Education"
    ENVIRONMENTAL = "Environmental"
    HEALTH = "Health"
    HUMAN_AND_CIVIL_RIGHTS = "Human and Civil Rights"
    HUMAN_SERVICES = "Human Services"
    INTERNATIONAL = "International"
    LATINO_RIGHTS = "Latino Rights"
    RESEARCH_AND_PUBLIC_POLICY = "Research and Public Policy"
    RELIGION = "Religion"
    WOMENS_RIGHTS = "Women's Rights"
    CAUSE_DROPDOWN_CHOICES =[(ANIMALS, "Animals"),(ARTS_CULTURE_HUMANITIES, "Arts Culture Humanities"),(ASIAN_RIGHTS,"Asian Rights"),
    (BLACK_RIGHTS, "Black Rights"),(COMMUNITY_DEVELOPMENT,"Community Development"),(EDUCATION, "Education"),
    (ENVIRONMENTAL, "Environmental"),(HEALTH,"Health"),(HUMAN_AND_CIVIL_RIGHTS, "Human and Civil Rights"),(HUMAN_SERVICES, "Human Services"),
    (INTERNATIONAL, "International"),(LATINO_RIGHTS,"Latino Rights"),(RESEARCH_AND_PUBLIC_POLICY, "Research and Public Policy"),
    (RELIGION, "Religion"),(WOMENS_RIGHTS,"Women's Rights")]

    cause = models.CharField(max_length=200, blank= True, choices=CAUSE_DROPDOWN_CHOICES)

    def __str__(self):
        return self.cause

class DonationRecord(models.Model):
    amountdonated = models.IntegerField()
    created_at = models.DateField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE, null=True, blank=True, related_name = "organizationdonationrecord" )
    goal = models.ForeignKey(DonationGoal,on_delete=models.CASCADE, null=True, blank=True, related_name = "drecord" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "duser", blank=True, null=True)
    cause = models.ForeignKey(Cause,on_delete=models.CASCADE, null=True, blank=True, related_name = "causedonationrecord" )

    def __str__(self):
        return f"Donated ${str(self.amountdonated)} to {self.organization}"

class VolunteerRecord(models.Model):
    hours = models.IntegerField()
    created_at = models.DateField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE, null=True, blank=True, related_name = "organizationvolunteerrecord" )
    description = models.CharField(max_length=1000, blank=True, null=True)
    goal = models.ForeignKey(VolunteerGoal,on_delete=models.CASCADE, null=True, blank=True, related_name = "vrecord" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "vuser", blank=True, null=True)
    cause = models.ForeignKey(Cause,on_delete=models.CASCADE, null=True, blank=True, related_name = "causevolunteerrecord" )

    def __str__(self):
        return f"Volunteered {str(self.hours)} for {self.organization}"

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField(upload_to="reciepts")
    dreceipt = models.ForeignKey(DonationRecord, null=True, on_delete=models.CASCADE, related_name='dreceipt')
    vreceipt = models.ForeignKey(VolunteerRecord, null=True, on_delete=models.CASCADE, related_name='vreceipt')

class EmailReminder(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='user')
    email = models.EmailField()
    subscribe = models.BooleanField(default=True)
    your_reminder = models.CharField(null=True, max_length=1000)
    WEEK = "Weekly"
    BIWEEKLY = "BiWeekly"
    MONTH = "Monthly"
    YEAR = "Yearly"
    INTERVAL = [(WEEK,"Weekly"),(BIWEEKLY, "BiWeekly"),(MONTH, "Monthly"), (YEAR, "Yearly")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL)

    def __str__(self):
        return self.your_reminder    

    def mail_create(self):
        if self.subscribe == True:
            mail_create.apply_async()
            # send_mail(
            #     subject=('Friendly Reminder from Charitable Tracker'),
            #     message=(f'Hi {self.user}. {self.your_reminder}.'),
            #     from_email=settings.EMAIL_HOST_USER,
            #     recipient_list=[self.email]
            #     )



