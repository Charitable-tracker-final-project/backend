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

    imgreciept = models.TextField(blank=True, null=True)
    # Donation Record Fields

    amountdonated = models.IntegerField(null=True)
    created_at = models.DateField()

    # Volunteer Record Fields

    hoursdonated = models.IntegerField(null=True)
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


#imgupload


    # def __str__(self):
    #     return self.organization

    # def __str__(self):
    #     return self.cause

    # def __str__(self):
    #     return f"Donated ${str(self.amountdonated)} to {self.organization}"

    # def __str__(self):
    #     return f"Volunteered {str(self.hoursdonated)} for {self.organization}"



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



