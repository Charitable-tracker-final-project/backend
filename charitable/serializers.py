from .models import User, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal
from rest_framework import serializers

class DonationGoalsSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Donationgoal
        fields = (
            "pk",
            "user",
            "goaltitle",
            "donationgoal",
            "interval"
        )

class VolunteerGoalsSerializers(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Volunteergoal
        fields = (
            "pk",
            "user",
            "goaltitle",
            "volunteergoal",
            "interval"
        )

class DonationRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Donationrecord
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "donationreceipt",
            "cause",
            "donationrecord"
        )

class VolunteerRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Volunteerrecord
        fields = (
            "pk",
            "hours",
            "created_at",
            "organization",
            "description",
            "volunteerreceipt",
            "cause",
            "volunteerrecord"
        )

class DonationGoalBreakdownSerializer(serializers.ModelSerializer):
    drecord = DonationRecordSerializers(many=True, required=False)
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username
        
    class Meta:
        model = Donationgoal
        fields = (
            "pk",
            "user",
            "goaltitle",
            "donationgoal",
            "interval",
            "drecord"
        )