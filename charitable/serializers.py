from .models import Emailreminder, Profile, User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal, Document, Emailreminder
from rest_framework import serializers

class DonationGoalsSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Donationgoal
        fields = (
            "pk",
            "goaltitle",
            "donationgoal",
            "interval",
            'created_at',
        )

class VolunteerGoalsSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Volunteergoal
        fields = (
            "pk",
            "goaltitle",
            "volunteergoal",
            "interval",
            'created_at',
        )

class DonationRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)


    class Meta:
        model = Donationrecord
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "cause",
            "donationrecord"
        )

class VolunteerRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)


    
    class Meta:
        model = Volunteerrecord
        fields = (
            "pk",
            "hours",
            "created_at",
            "organization",
            "description",
            "cause",
            "volunteerrecord"
        )

class DonationGoalBreakdownSerializer(serializers.ModelSerializer):
    drecord = DonationRecordSerializers(many=True, required=False)
    
        
    class Meta:
        model = Donationgoal
        fields = (
            "pk",
            "goaltitle",
            "donationgoal",
            "interval",
            "drecord"
        )


class VolunteerGoalBreakdownSerializer(serializers.ModelSerializer):
    vrecord = VolunteerRecordSerializers(many=True, required=False)
    
        
    class Meta:
        model = Volunteergoal
        fields = (
            "pk",
            "goaltitle",
            "volunteergoal",
            "interval",
            "vrecord"
        )

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = (
            "annual_income",
            )


class DocumentSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(required=False)
    
    class Meta:
        model = Document 
        fields = (
            "upload",
        )

class EmailReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emailreminder
        fields = (
            "email",
            "subscribe",
            "frequency",
            "your_reminder"
        )


class OrganizationTimeSerializers(serializers.ModelSerializer):


    class Meta:
        model = Volunteerrecord
        fields = (
            "hours",
            "organization",
        )

class OrganizationDonationSerializers(serializers.ModelSerializer):


    class Meta:
        model = Donationrecord
        fields = (
            "amountdonated",
            "organization",
        )

class CauseTimeSerializers(serializers.ModelSerializer):


    class Meta:
        model = Volunteerrecord
        fields = (
            "hours",
            "cause",
        )

class CauseDonationSerializers(serializers.ModelSerializer):


    class Meta:
        model = Donationrecord
        fields = (
            "amountdonated",
            "cause",
        )