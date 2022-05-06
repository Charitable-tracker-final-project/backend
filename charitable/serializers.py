from .models import EmailReminder, Profile, Record, User, Goal, Document, EmailReminder
from rest_framework import serializers
from django.db.models import Q, Avg, Max, Min, Sum, F


class VolunteerGoalSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)

    class Meta:
        model = Goal
        fields = (
            "pk",
            "vgoaltitle",
            "hours",
            "interval",
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
            "interval",
            'created_at',
        )

        
class DonationRecordSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    goal = serializers.SlugRelatedField(slug_field='dgoaltitle', read_only=True )
    

    class Meta:
        model = Record
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "cause",
            "goal",
            "imgreciept",
        )

class VolunteerRecordSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    #goal = serializers.SlugRelatedField(slug_field='vgoaltitle', read_only=True)
    

    class Meta:
        model = Record
        fields = (
            "pk",
            "hoursdonated",
            "created_at",
            "organization",
            "description",
            "cause",
            "goal",
            "imgreciept",
        )

class DonationGoalBreakdownSerializer(serializers.ModelSerializer):
    record = DonationRecordSerializer(many=True, required=False)
    totaldonated = serializers.SerializerMethodField()


    class Meta:
        model = Goal
        fields = (
            "pk",
            "dgoaltitle",
            "dollars",
            "interval",
            "record",
            "totaldonated",
        )

    def get_totaldonated(self, goal):
        # total = Record.objects.aggregate(sum_donated=Sum('amountdonated'))
        return goal.record.aggregate(sum_donated=Sum('amountdonated'))
        


class VolunteerGoalBreakdownSerializer(serializers.ModelSerializer):
    record = VolunteerRecordSerializer(many=True, required=False)
    timedonated = serializers.SerializerMethodField()
        
    class Meta:
        model = Goal
        fields = (
            "pk",
            "hours",
            "vgoaltitle",
            "interval",
            "record",
            "timedonated",
        )

    def get_timedonated(self, goal):
        return goal.record.aggregate(sum_donated=Sum('hoursdonated'))

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
        model = Goal
        fields = (
        "organization",
        "donationgoal",
        "volunteergoal",
        )


class CauseSerializer(serializers.ModelSerializer):
    donationgoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)
    volunteergoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)

    class Meta:
        model = Record
        fields = (
            "cause",
            "donationgoal",
            "volunteergoal",
        )

class OrganizationDonationSerializer(serializers.ModelSerializer):
    totaldonated = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = (
            "pk",
            "organization",
            "amountdonated",
            "totaldonated",
        )
    def get_totaldonated(self, instance):
        return Record.objects.filter(user=self.context["request"].user, organization=instance.organization).aggregate(sum_donated=Sum('amountdonated'))


class OrganizationTimeSerializer(serializers.ModelSerializer):
    timedonated = serializers.SerializerMethodField()


    class Meta:
        model = Record
        fields = (
            "pk",
            "organization",
            "hoursdonated",
            "timedonated",
        )

    def get_timedonated(self, instance):
        return Record.objects.filter(user=self.context["request"].user, organization=instance.organization).aggregate(sum_donated=Sum('hoursdonated'))



class CauseTimeSerializer(serializers.ModelSerializer):
    causevolunteerrecord=VolunteerRecordSerializer(many=True, required=False)

    class Meta:
        model = Record
        fields = (
            "cause",
            "causevolunteerrecord",
        )

class CauseDonationSerializer(serializers.ModelSerializer):
    #totaldonated = serializers.SerializerMethodField() 
    sum_donated = serializers.IntegerField()

    class Meta:
        model = Record
        fields = (
            "pk",
            "cause",
            "amountdonated",
            "sum_donated"
        )
    def get_totaldonated(self, cause):
        return Record.objects.filter().annotate(sum_donated=Sum('amountdonated'))

    def get_totaldonated(self, instance):
        return Record.objects.filter(
            user=self.context["request"].user, cause=instance.cause
        ).aggregate(Sum("amountdonated"))



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
