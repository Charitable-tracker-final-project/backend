from .models import Cause, Org, EmailReminder, Profile, Record, User, Goal, Document, EmailReminder
from rest_framework import serializers
from django.db.models import Q, Avg, Max, Min, Sum, Case, When, Value, CharField, F
import calendar
from django.db.models.functions import ExtractMonth


class VolunteerGoalSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Goal
        fields = (
            "pk",
            "vgoaltitle",
            "hours",
            'created_at',
            
        )

class DonationGoalSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Goal
        fields = (
            "pk",
            "dgoaltitle",
            "dollars",
            'created_at',
        )

    

        
class DonationRecordSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Record
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "cause",
            "alldonated",
            "imgreciept",
        )

    

class VolunteerRecordSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    

    class Meta:
        model = Record
        fields = (
            "pk",
            "hoursdonated",
            "created_at",
            "organization",
            "description",
            "cause",
            "allhours",
            "imgreciept",
        )

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "pk",
            "annual_income",
            "profile_pic",
            )


class DocumentSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(required=False)
    
    class Meta:
        model = Document 
        fields = (
            "pk",
            "upload",
            "dreceipt",
            "vreceipt", 
        )

class EmailReminderSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = EmailReminder
        fields = (
            "pk",
            "email",
            "subscribe",
            "interval",
            "message",
            
        )


class OrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = (
        "organization",
        )


class CauseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = (
            "cause",
        )


class OrgTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = (
            "organization",
            "total_by_org_time",
            "allhours",
        )



class CauseTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = (
            "cause",
            "total_by_cause_time",
            "allhours",
        )
    

class CauseDonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cause
        fields = (
            "cause",
            "total_by_cause_donated",
            "alldonated",
        )


class OrgDonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = (
            "organization",
            "total_by_org_donated",
            "alldonated",
        )

class AllRecords(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields= (
            "user",
            "goal",
            "amountdonated",
            "created_at",
            "hoursdonated",
            "description",
            "cause",
            "organization"
        )

    






