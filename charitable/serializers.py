from .models import EmailReminder, Profile, Record, User, Goal, Document, EmailReminder
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
    alldonated = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = (
            "pk",
            "amountdonated",
            "created_at",
            "organization",
            "cause",
            "goal",
            "alldonated",
        )

    def get_alldonated(self, goal):
        return Record.objects.aggregate(alldonated=Sum('amountdonated'))

class VolunteerRecordSerializer(serializers.ModelSerializer):
    created_at=serializers.DateField(format="%Y-%m-%d", required=False)
    goal = serializers.SlugRelatedField(slug_field='vgoaltitle', read_only=True)
    

    class Meta:
        model = Record
        fields = (
            "pk",
            "hoursdonated",
            "created_at",
            "organization",
            "description",
            "cause",
            "goal"
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
        # breakpoint()
        # dollars = Goal.objects.first('dollars')
        sum = goal.record.aggregate(totaldonos=Sum('amountdonated'))
        return sum
        


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
    cause = serializers.SlugRelatedField(slug_field='title', read_only=True)
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
        return Record.objects.filter(user=self.context["request"].user, organization=instance.organization).aggregate(totaldonos=Sum('amountdonated'))


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
        return Record.objects.filter(user=self.context["request"].user, organization=instance.organization).aggregate(totaldonos_org=Sum('hoursdonated'))



class CauseTimeSerializer(serializers.ModelSerializer):
    timedonated = serializers.SerializerMethodField()

    class Meta:
        model = Record
        fields = (
            "pk",
            "cause",
            "hoursdonated",
            "timedonated",
        )
    
    def get_timedonated(self, instance):
        return Record.objects.filter(user=self.context["request"].user, cause=instance.cause).aggregate(totaldonos_org=Sum('hoursdonated'))


class CauseDonationSerializer(serializers.ModelSerializer):
    totaldonated = serializers.SerializerMethodField()
    alldonated = serializers.SerializerMethodField()
    months = serializers.SerializerMethodField()
    

    class Meta:
        model = Record
        fields = (
            "cause",
            "totaldonated",
            "amountdonated",
            "alldonated",
            "months",
        )

    def get_totaldonated(self, instance):
        return Record.objects.filter(user=self.context["request"].user, cause=instance.cause).aggregate(totaldono_cause=Sum('amountdonated'))

    def get_alldonated(self, instance):
        return Record.objects.aggregate(alldonos=Sum('amountdonated'))

    def get_months(self, instance):
        conditions = []
        for i in range(1, 13):
            month_name = calendar.month_name[i]
            conditions.append(When(created_at__month=i, then=Value(month_name)))

        return Record.objects.filter(user=self.context["request"].user, amountdonated=instance.amountdonated).annotate(month_name=Case(*conditions, default=Value(""), output_field=CharField())
        ).order_by("month_name").values_list("month_name", flat=True).distinct()

    
    #     months = (
    #         Record.objects
    #         .filter(created_at__gte=start, created_at__lte=end)
    #         .annotate(month=ExtractMonth('some_datetime_field'))
    #         .values_list('month', flat=True)
    #         .distinct()
    #     )
    #     return months





