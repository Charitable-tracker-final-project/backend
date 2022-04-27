from .models import Profile, User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal, Document
from rest_framework import serializers

class DonationGoalsSerializers(serializers.ModelSerializer):


    class Meta:
        model = Donationgoal
        fields = (
            "pk",
            "goaltitle",
            "donationgoal",
            "interval"
        )

class VolunteerGoalsSerializers(serializers.ModelSerializer):


    class Meta:
        model = Volunteergoal
        fields = (
            "pk",
            "goaltitle",
            "volunteergoal",
            "interval"
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
    upload = serializers.ImageField()
    
    class Meta:
        model = Document 
        fields = (
            "upload",
        )