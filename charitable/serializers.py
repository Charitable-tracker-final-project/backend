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
    # goal = serializers.SlugRelatedField(slug_field='dgoaltitle', read_only=True )

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
    # goal = serializers.SlugRelatedField(slug_field='vgoaltitle', read_only=True)
    

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

class DonationGoalBreakdownSerializer(serializers.ModelSerializer):
    record = DonationRecordSerializer(many=True, required=False)
    totaldonated = serializers.SerializerMethodField()


    class Meta:
        model = Goal
        fields = (
            "pk",
            "dgoaltitle",
            "dollars",

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
            "message",
            
        )


# class OrganizationSerializer(serializers.ModelSerializer):
#     donationgoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)

#     class Meta:
#         model = Goal
#         fields = (
#         "organization",
#         "donationgoal",
#         "volunteergoal",
#         )


# class CauseSerializer(serializers.ModelSerializer):
#     cause = serializers.SlugRelatedField(slug_field='title', read_only=True)
#     volunteergoal = serializers.SlugRelatedField(slug_field='goaltitle', read_only=True)

#     class Meta:
#         model = Record
#         fields = (
#             "cause",
#             "donationgoal",
#             "volunteergoal",
#         )

    

# class OrganizationDonationSerializer(serializers.ModelSerializer):
#     totaldonated = serializers.SerializerMethodField()

#     class Meta:
#         model = Record
#         fields = (
#             "pk",
#             "organization",
#             "amountdonated",
#             "totaldonated",
#         )
#     def get_totaldonated(self, instance):
#         return Record.objects.filter(user=self.context["request"].user, organization=instance.organization).aggregate(totaldonos=Sum('amountdonated'))


class OrgTimeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Org
        fields = (
            "organization",
            "total_by_org_time",
            "all_hours",
        )



class CauseTimeSerializer(serializers.ModelSerializer):
    # timedonated = serializers.SerializerMethodField()

    class Meta:
        model = Cause
        fields = (
            "cause",
            "total_by_cause_time",
            "all_hours",
        )
    
    # def get_timedonated(self, instance):
    #     return Record.objects.filter(user=self.context["request"].user, cause=instance.cause).aggregate(totaldonos_org=Sum('hoursdonated'))


class CauseDonationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Cause
        fields = (
            "cause",
            "total_by_cause_donated",
            "all_donated",
        )


    # def get_months(self, instance):
    #     conditions = []
    #     for i in range(1, 13):
    #         month_name = calendar.month_name[i]
    #         conditions.append(When(created_at__month=i, then=Value(month_name)))

    #     return Record.objects.filter(user=self.context["request"].user, amountdonated=instance.amountdonated).annotate(month_name=Case(*conditions, default=Value(""), output_field=CharField())
    #     ).order_by("month_name").values_list("month_name", flat=True).distinct()

class OrgDonationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Org
        fields = (
            "organization",
            "total_by_org_donated",
            "all_donated",
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

# class DonationCauseDonationRecordSerializer(serializers.ModelSerializer):
#     cause = CauseDonationSerializer(many=True, required=False)
#     all_donated = serializers.SerializerMethodField()

#     class Meta:
#         model = CauseDonation
#         fields = (
#             "all_donated",
#             "cause"
#         )

#     def all_donated(self):
#         return Record.objects.filter(user=self.user).aggregate(Sum('amountdonated'))
    






