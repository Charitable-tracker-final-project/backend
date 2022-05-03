from ast import And
from xml.etree.ElementInclude import include
from django.shortcuts import render
from rest_framework.views import APIView
from django.core.paginator import Paginator
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
    Cause,
    Organization,
    User,
    Profile,
    DonationRecord,
    VolunteerRecord,
    VolunteerGoal,
    DonationGoal,
    Document,
    EmailReminder
)
from .serializers import ( 
    DonationGoalsSerializers,
    VolunteerGoalsSerializers,
    DonationRecordSerializers,
    VolunteerRecordSerializers,
    DonationGoalBreakdownSerializer,
    ProfileSerializer,
    VolunteerGoalBreakdownSerializer,
    DocumentSerializer,
    EmailReminderSerializer,
    CauseTimeSerializer,
    CauseDonationSerializer,
    OrganizationDonationSerializer,
    OrganizationTimeSerializer,
)
from django.db.models import Q, Avg, Max, Min, Sum
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



class DonationGoalListView(generics.ListCreateAPIView):
    queryset = DonationGoal.objects.all()
    serializer_class = DonationGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return DonationGoal.objects.filter(filters).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonationGoal.objects.all()
    serializer_class = DonationGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return DonationGoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalListView(generics.ListCreateAPIView):
    queryset = VolunteerGoal.objects.all()
    serializer_class = VolunteerGoalsSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return VolunteerGoal.objects.filter(filters).order_by('-created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerGoal.objects.all()
    serializer_class = VolunteerGoalsSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return VolunteerGoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationRecordListView(generics.ListCreateAPIView):
    serializer_class = DonationRecordSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return DonationRecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationRecordSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return DonationRecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerRecordListView(generics.ListCreateAPIView):
    serializer_class = VolunteerRecordSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteerrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerRecord.objects.all()
    serializer_class = VolunteerRecordSerializers


    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return VolunteerRecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user) 
        return DonationGoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DonationGoalSumBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user) 
        return DonationGoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VolunteerGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VolunteerGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return VolunteerGoal.objects.filter(filters)
    
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


class OrganizationTime(generics.ListAPIView):
    serializer_class = OrganizationTimeSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Organization.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrganizationDonationview(generics.ListAPIView):
    serializer_class = OrganizationDonationSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user) 
        return Organization.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class CauseTime(generics.ListAPIView):
    serializer_class = CauseTimeSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Cause.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseDonation(generics.ListAPIView):
    serializer_class = CauseDonationSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user) 
        return Cause.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




