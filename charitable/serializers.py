from .models import EmailReminder, Organization, Cause, Profile, User, DonationRecord, VolunteerRecord, VolunteerGoal, DonationGoal, Document, EmailReminder
from rest_framework import serializers
from django.db.models import Q, Avg, Max, Min, Sum

class DonationGoalsSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = DonationGoal
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
        model = VolunteerGoal
        fields = (
            "pk",
            "goaltitle",
            "volunteergoal",
            "interval",
            'created_at',
        )

class DonationRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    donationrecord = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)
    organization = serializers.SlugRelatedField(slug_field='organization', read_only=True)
    cause = serializers.SlugRelatedField(slug_field='cause', read_only=True)
    

    class Meta:
        model = DonationRecord
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "cause",
            "donationrecord",
        )

class VolunteerRecordSerializers(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    volunteerrecord = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)
    organization = serializers.SlugRelatedField(slug_field='organization', read_only=True)
    cause = serializers.SlugRelatedField(slug_field='cause', read_only=True)

    class Meta:
        model = VolunteerRecord
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
    totaldonated = serializers.SerializerMethodField()


    class Meta:
        model = DonationGoal
        fields = (
            "pk",
            "goaltitle",
            "donationgoal",
            "interval",
            "drecord",
            "totaldonated",
        )
    
    def get_totaldonated(self, obj):
        title = {'goaltitle'}
        return DonationRecord.objects.filter(title).aggregate(sum_donated=Sum('amountdonated'))

class VolunteerGoalBreakdownSerializer(serializers.ModelSerializer):
    vrecord = VolunteerRecordSerializers(many=True, required=False)
    
        
    class Meta:
        model = VolunteerGoal
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
            "your_reminder"
        )


class OrganizationSerializer(serializers.ModelSerializer):
    donationgoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)

    class Meta:
        model = Organization
        fields = (
        "organization",
        "donationgoal",
        "volunteergoal",
        )


class CauseSerializer(serializers.ModelSerializer):
    donationgoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)
    volunteergoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)

    class Meta:
        model = Cause
        fields = (
            "cause",
            "donationgoal",
            "volunteergoal",
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