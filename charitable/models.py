from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from charitable_tracker.storage_backends import PrivateMediaStorage
from charitable_tracker import settings
from django.core.mail import send_mail
from django.db.models import Q, Avg, Max, Min, Sum, Case, When, Value, CharField, F
from celery.schedules import crontab

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

class Goal(models.Model):
    created_at = models.DateField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "donor")

    #Donation Fields
    dgoaltitle = models.CharField(max_length=100, blank=True)
    dollars = models.IntegerField(null=True)

    # Volunteer Fields
    vgoaltitle = models.CharField(max_length=100, blank=True)
    hours = models.IntegerField(null=True)

    #intervaldropdownlist
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    INTERVAL_DROPDOWN_CHOICES = [(WEEK,"Week"),(MONTH, "Month"), (YEAR, "Year")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL_DROPDOWN_CHOICES)

    # def __str__(self):
    #     return self.vgoaltitle

    # def __str__(self):
    #     return self.dgoaltitle

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=["habit_record", "update_date"], name="one_record_per_day")
    #     ]


class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "duser", blank=True, null=True)
    goal = models.ForeignKey(Goal,on_delete=models.CASCADE, null=True, blank=True, related_name="record")

    #imgupload 
    imgreciept = models.TextField(blank=True, null=True)
    # Donation Record Fields

    amountdonated = models.IntegerField(null=True, blank=True)
    created_at = models.DateField()

    # Volunteer Record Fields

    hoursdonated = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=1000, blank=True, null=True)


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

    organization = models.CharField(max_length=200, blank=True)

    @property
    def alldonated(self):
        return Record.objects.filter(user=self.user).aggregate(alldonated=Sum('amountdonated'))

    @property
    def allhours(self):
        return Record.objects.filter(user=self.user).aggregate(allhours=Sum('hoursdonated'))


class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.ImageField(upload_to="reciepts")
    dreceipt = models.ForeignKey(Record, null=True, on_delete=models.CASCADE, related_name='dreceipt')
    vreceipt = models.ForeignKey(Record, null=True, on_delete=models.CASCADE, related_name='vreceipt')

class EmailReminder(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='user')
    email = models.EmailField()
    subscribe = models.BooleanField(default=True)
    message = models.CharField(null=True, max_length=1000)
    WEEK = "Weekly"
    BIWEEKLY = "BiWeekly"
    MONTH = "Monthly"
    YEAR = "Yearly"
    INTERVAL = [(WEEK,"Weekly"),(BIWEEKLY, "BiWeekly"),(MONTH, "Monthly"), (YEAR, "Yearly")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL)

    def __str__(self):
        return self.message


class Cause(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "causedonations", blank=True, null=True)

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

    @property
    def total_by_cause_donated(self):
        return Record.objects.filter(user=self.user, cause=self.cause).aggregate(Sum('amountdonated'))

    @property
    def total_by_cause_time(self):
        return Record.objects.filter(user=self.user, cause=self.cause).aggregate(Sum('hoursdonated'))

    @property
    def all_donated(self):
        return Record.objects.filter(user=self.user).aggregate(Sum('amountdonated'))

    @property
    def all_hours(self):
        return Record.objects.filter(user=self.user).aggregate(Sum('hoursdonated'))

    def __str__(self):
        return f'{self.cause} for {self.user}'
    



class Org(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "orgdonations", blank=True, null=True)

    organization = models.CharField(max_length=200, blank=True)

    @property
    def total_by_org_donated(self):
        return Record.objects.filter(user=self.user, organization=self.organization).aggregate(Sum('amountdonated'))

    @property
    def total_by_org_time(self):
        return Record.objects.filter(user=self.user, organization=self.organization).aggregate(Sum('hoursdonated'))

    @property
    def all_donated(self):
        return Record.objects.filter(user=self.user).aggregate(Sum('amountdonated'))

    @property
    def all_hours(self):
        return Record.objects.filter(user=self.user).aggregate(Sum('hoursdonated'))

    def __str__(self):
        return f'{self.organization} for {self.user}'





