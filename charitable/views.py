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
    ProfileSerializer,
    DocumentSerializer,
    EmailReminderSerializer,
    CauseTimeSerializer,
    CauseDonationSerializer,
    AllRecords,
    OrgTimeSerializer,
    OrgDonationSerializer,
    OrgSerializer,
    CauseSerializer,
)
from django.db.models import Q, Avg, Max, Min, Sum, Case, When, Value, CharField
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# class GoogleLogin(SocialLoginView): 
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
#     client_class = OAuth2Client

from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from rest_framework.parsers import FileUploadParser
from charitable_tracker import settings
from django.core.mail import send_mail
from .tasks import mail_create

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
        return Record.objects.filter(filters).exclude(amountdonated__isnull=True)

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
        return Record.objects.filter(filters).exclude(hoursdonated__isnull=True)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VolunteerRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = VolunteerRecordSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(filters)
    
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
        serializer.save(user=user, upload=self.request.FILES["file"])

class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):   
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = [FileUploadParser]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user, upload=self.request.FILES["file"])

class EmailReminderView(ListCreateAPIView):
    serializer_class = EmailReminderSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return EmailReminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        reminder = serializer.instance
        mail_create.apply_async(kwargs={'reminder_pk': reminder.pk})

class EmailReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailReminderSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return EmailReminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        reminder = serializer.instance
        mail_create.apply_async(kwargs={'reminder_pk': reminder.pk})


class OrgListCreateView(generics.ListCreateAPIView):
    serializer_class = OrgSerializer

    def get_queryset(self):
        return Org.objects.filter(user=self.request.user).distinct("cause")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseListCreateView(generics.ListCreateAPIView):
    serializer_class = CauseSerializer

    def get_queryset(self):
        return Cause.objects.filter(user=self.request.user).distinct("cause")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseDonationListView(generics.ListAPIView):
    serializer_class = CauseDonationSerializer

    def get_queryset(self):
        return Cause.objects.filter(user=self.request.user).distinct("cause")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseTimeListView(generics.ListAPIView):
    serializer_class = CauseTimeSerializer

    def get_queryset(self):
        return Cause.objects.filter(user=self.request.user).distinct("cause")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrgDonationListView(generics.ListAPIView):
    serializer_class = OrgDonationSerializer

    def get_queryset(self):
        return Org.objects.filter(user=self.request.user).distinct("organization")
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrgTimeListView(generics.ListAPIView):
    serializer_class = OrgTimeSerializer

    def get_queryset(self):
        return Org.objects.filter(user=self.request.user).distinct("organization")
    
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




