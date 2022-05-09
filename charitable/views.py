from itertools import filterfalse
from django.shortcuts import render
from rest_framework.views import APIView
from django.core.paginator import Paginator
from rest_framework.decorators import action
from rest_framework.response import Response
import calendar
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, timedelta

from rest_framework import (
    generics,
    permissions, 
    viewsets,
    filters,
    status,
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    CreateAPIView
)
from .models import (
    User,
    Profile,
    Record,
    Goal,
    Document,
    EmailReminder,
    Cause, 
    Org,
)
from .serializers import ( 
    DonationGoalSerializer,
    VolunteerGoalSerializer,
    DonationRecordSerializer,
    VolunteerRecordSerializer,
    DonationGoalBreakdownSerializer,
    ProfileSerializer,
    VolunteerGoalBreakdownSerializer,
    DocumentSerializer,
    EmailReminderSerializer,
    CauseTimeSerializer,
    CauseDonationSerializer,
    AllRecords,
    OrgTimeSerializer,
    OrgDonationSerializer,
)
from django.db.models import Q, Avg, Max, Min, Sum, Case, When, Value, CharField
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

class GoogleLogin(SocialLoginView): 
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
    client_class = OAuth2Client

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework.parsers import FileUploadParser
from django.core.mail import send_mail
from charitable_tracker import settings

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class RecordResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10

class DonationGoalListView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = DonationGoalSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Goal.objects.filter(filters).order_by('-created_at').exclude(dollars=None)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = DonationGoalSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Goal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalListView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = VolunteerGoalSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Goal.objects.filter(filters).order_by('created_at').exclude(hours=None)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = VolunteerGoalSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Goal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class DonationRecordListView(generics.ListCreateAPIView):
    serializer_class = DonationRecordSerializer
    pagination_class = RecordResultsSetPagination

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Record.objects.filter(user=self.request.user).exclude(amountdonated__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationRecordSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerRecordListView(generics.ListCreateAPIView):
    serializer_class = VolunteerRecordSerializer
    pagination_class = RecordResultsSetPagination

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(user=self.request.user).exclude(hoursdonated__isnull=True)
    
    def perform_create(self, serializer):
        goal = self.request.user.donor.first()
        serializer.save(user=self.request.user, goal=goal)



class VolunteerRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = VolunteerRecordSerializer

    
    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DonationGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user) 
        return Goal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DonationGoalSumBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer

    def get_queryset(self):
        # queryset = queryset.filter(goltitle__contains=)
        # filters = Q(user_id=queryset)
        filters = Q(user_id=self.request.user) 
        return Goal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VolunteerGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VolunteerGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Goal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnnualIncomeView(generics.ListCreateAPIView):   
    serializer_class = ProfileSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Profile.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnnualIncomeDetailView(generics.RetrieveUpdateDestroyAPIView):   
    serializer_class = ProfileSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Profile.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentCreateView(ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = [FileUploadParser]

    def perform_create(self, serializer):
        user = self.request.user
        # the following line is a placeholder until you are able to access a logged in user
        # user = User.objects.first()
        serializer.save(user=user, upload=self.request.FILES["file"])

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = [FileUploadParser]

    def perform_create(self, serializer):
        user = self.request.user
        # the following line is a placeholder until you are able to access a logged in user
        # user = User.objects.first()
        serializer.save(user=user, upload=self.request.FILES["file"])

class EmailReminderView(ListCreateAPIView):
    serializer_class = EmailReminderSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return EmailReminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        reminder = serializer.instance
        reminder.mail_create()

class EmailReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailReminderSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return EmailReminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        reminder = serializer.instance
        reminder.mail_create()


# class OrganizationTime(generics.ListAPIView):
#     serializer_class = OrgTimeSerializer

#     def get_queryset(self):
#         search_term = self.request.query_params.get("organization")
#         return Record.objects.filter(user=self.request.user, organization__iexact = search_term)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class OrganizationDonationview(generics.ListAPIView):
#     serializer_class = OrgDonationSerializer

#     def get_queryset(self):
#         search_term = self.request.query_params.get("organization")
#         return Record.objects.filter(user=self.request.user, organization__iexact = search_term)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    

# class CauseTime(generics.ListAPIView):
#     serializer_class = CauseTimeSerializer

#     def get_queryset(self):
#         search_term = self.request.query_params.get("cause")
#         return Record.objects.filter(cause__iexact = search_term, user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class CauseDonationListView(generics.ListAPIView):
    serializer_class = CauseDonationSerializer

    def get_queryset(self):
        # search_term = self.request.query_params.get("cause")
        # return Record.objects.filter(user=self.request.user, cause__iexact = search_term)
        # amountdonated = self.request.user.donor.exclude(amountdonated=None)

        # conditions = []
        # for i in range(1, 13):
        #     month_name = calendar.month_name[i]
        #     conditions.append(When(created_at__month=i, then=Value(month_name)))

        # return Record.objects.annotate(month_name=Case(*conditions, default=Value(""), output_field=CharField())
        # ).order_by("month_name").values_list("month_name", flat=True).distinct().filter(user=self.request.user).exclude(amountdonated=None)

        return Cause.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseTimeListView(generics.ListAPIView):
    serializer_class = CauseTimeSerializer

    def get_queryset(self):
        return Cause.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrgDonationListView(generics.ListAPIView):
    serializer_class = OrgDonationSerializer

    def get_queryset(self):
        return Org.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrgTimeListView(generics.ListAPIView):
    serializer_class = OrgTimeSerializer

    def get_queryset(self):
        return Org.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)





class AllRecords(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = AllRecords
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Record.objects.filter(filters)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class  DonationCauseDonationRecord(generics.ListAPIView):
#     serializer_class = DonationCauseDonationRecordSerializer

#     def get_queryset(self):
#         return CauseDonation.objects.filter(user=self.request.user)
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)




