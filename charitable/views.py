from xml.etree.ElementInclude import include
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import (
    generics,
    permissions, 
    viewsets,
    filters,
    status
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
    Donationrecord,
    Volunteerrecord,
    Volunteergoal,
    Donationgoal,
    Document,
    Emailreminder
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
    OrganizationTimeSerializers,
    OrganizationDonationSerializers,
    CauseTimeSerializers,
    CauseDonationSerializers,
)
from django.db.models import Q
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
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationgoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationgoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalListView(generics.ListCreateAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteergoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteergoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationRecordListView(generics.ListCreateAPIView):
    serializer_class = DonationRecordSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationRecordSerializers

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Donationrecord.objects.filter(filters)
    
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
    queryset = Volunteerrecord.objects.all()
    serializer_class = VolunteerRecordSerializers


    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteerrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DonationGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Donationgoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VolunteerGoalBreakdownView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VolunteerGoalBreakdownSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Volunteergoal.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnnualIncomeView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()    
    serializer_class = ProfileSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Profile.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DocumentCreateView(CreateAPIView):
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
        return Emailreminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class OrganizationTime(generics.ListAPIView):
    serializer_class = OrganizationTimeSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Volunteerrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class OrganizationDonation(generics.ListAPIView):
    serializer_class = OrganizationDonationSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class EmailReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmailReminderSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Emailreminder.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseTime(generics.ListAPIView):
    serializer_class = CauseTimeSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Volunteerrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseDonation(generics.ListAPIView):
    serializer_class = CauseDonationSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationrecord.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerAllGoalListView(generics.ListCreateAPIView):
    serializer_class = VolunteerGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Volunteergoal.objects.filter(filters).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DonationAllGoalListView(generics.ListCreateAPIView):
    serializer_class = DonationGoalsSerializers

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Donationgoal.objects.filter(filters).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
