from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    email = models.EmailField(max_length=250)
    
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_profile")
    annual_income = models.IntegerField(null=True, blank=True)

class Donationgoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "donor")
    goaltitle = models.CharField(max_length=100, blank=True)
    donationgoal = models.IntegerField()

    #intervaldropdownlist
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    INTERVAL_DROPDOWN_CHOICES = [(WEEK,"Week"),(MONTH, "Month"), (YEAR, "Year")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL_DROPDOWN_CHOICES)

    def __str__(self):
        return self.goaltitle

class Volunteergoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "volunteer")
    goaltitle = models.CharField(max_length=100, blank=True)
    volunteergoal = models.IntegerField()

    #intervaldropdownlist
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"
    INTERVAL_DROPDOWN_CHOICES = [(WEEK,"Week"),(MONTH, "Month"), (YEAR, "Year")]
    interval = models.CharField(max_length=200, blank=True, choices=INTERVAL_DROPDOWN_CHOICES)

    def __str__(self):
        return self.goaltitle

class Donationrecord(models.Model):
    amountdonated = models.IntegerField()
    created_at = models.DateField()
    organization = models.CharField(max_length=200, blank=True)
    donationreceipt = models.ImageField(upload_to='reciepts', blank=True, null=True)
    donationrecord = models.ForeignKey(Donationgoal,on_delete=models.CASCADE, null=True, blank=True, related_name = "drecord" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "duser", blank=True, null=True)

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
        return f"Donated ${str(self.amountdonated)} to {self.organization}"

class Volunteerrecord(models.Model):
    hours = models.IntegerField()
    created_at = models.DateField()
    organization = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    volunteerreceipt = models.ImageField(upload_to='reciepts', blank=True, null=True)
    volunteerrecord = models.ForeignKey(Volunteergoal,on_delete=models.CASCADE, null=True, blank=True, related_name = "vrecord" )

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
    (BLACK_RIGHTS, "Black Rights"),(COMMUNITY_DEVELOPMENT,"Community Development"),(EDUCATION, "Education"),(ENVIRONMENTAL, "Environmental"),
    (HEALTH,"Health"),(HUMAN_AND_CIVIL_RIGHTS, "Human and Civil Rights"),(HUMAN_SERVICES, "Human Services"),
    (INTERNATIONAL, "International"),(LATINO_RIGHTS,"Latino Rights"),(RESEARCH_AND_PUBLIC_POLICY, "Research and Public Policy"),
    (RELIGION, "Religion"),(WOMENS_RIGHTS,"Women's Rights")]

    cause = models.CharField(max_length=200, blank= True, choices=CAUSE_DROPDOWN_CHOICES)

    def __str__(self):
        return f"Volunteered {str(self.hours)} for {self.organization}"