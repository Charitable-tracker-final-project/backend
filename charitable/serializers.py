from .models import Emailreminder, Organization, Cause, Profile, User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal, Document, Emailreminder
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
        )

class EmailReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Emailreminder
        fields = (
            "pk",
            "email",
            "subscribe",
            "interval",
            "your_reminder"
        )



class OrganizationDonationSerializer(serializers.ModelSerializer):
    organizationdonationrecord=DonationRecordSerializers(many=True, required=False)

    class Meta:
        model = Organization
        fields = (
        "organization",
        "organizationdonationrecord",
        )


class OrganizationTimeSerializer(serializers.ModelSerializer):
    organizationvolunteerrecord=VolunteerRecordSerializers(many=True, required=False)

    class Meta:
        model = Organization
        fields = (
        "organization",
        "organizationvolunteerrecord",
        )



class CauseTimeSerializer(serializers.ModelSerializer):
    causevolunteerrecord=VolunteerRecordSerializers(many=True, required=False)

    class Meta:
        model = Cause
        fields = (
            "cause",
            "causevolunteerrecord",
        )

class CauseDonationSerializer(serializers.ModelSerializer):
    causedonationrecord=DonationRecordSerializers(many=True, required=False)

    class Meta:
        model = Cause
        fields = (
            "cause",
            "causedonationrecord",
        )