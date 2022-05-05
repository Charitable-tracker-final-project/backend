from django.shortcuts import render
from rest_framework.views import APIView
from django.core.paginator import Paginator
from rest_framework.decorators import action
from rest_framework.response import Response

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
    EmailReminder
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
    queryset = Goal.objects.all()
    serializer_class = DonationGoalSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Goal.objects.filter(filters).order_by('-created_at')
    
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
        return Goal.objects.filter(filters).order_by('-created_at')
    
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
    # queryset = Record.objects.all()

    # @action(detail=False, methods=["GET"])
    # def get_queryset(self, request):
    #     '''
    #     Using this to create a seperate, custom 
    #     enpoint for only a Users records
    #     GET  /api/Drecords/
    #     '''
    #     record = self.get_queryset().filter(user_id=self.request.user)
    #     serializer = self.get_serializer(record, many=True)
    #     return Response(serializer.data)
    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Record.objects.filter(filters)

    def perform_create(self, serializer):
        goal = self.request.user.donor.last()
        serializer.save(user=self.request.user, goal=goal)

class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DonationRecordSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VolunteerRecordListView(generics.ListCreateAPIView):
    serializer_class = VolunteerRecordSerializer

    def get_queryset(self):
        filters = Q(user_id=self.request.user)
        return Record.objects.filter(filters)
    
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


class OrganizationTime(generics.ListAPIView):
    serializer_class = OrganizationTimeSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Record.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrganizationDonationview(generics.ListAPIView):
    serializer_class = OrganizationDonationSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("organization")
        return Record.objects.filter(user=self.request.user, organization__iexact = search_term)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class CauseTime(generics.ListAPIView):
    serializer_class = CauseTimeSerializer

    def get_queryset(self):
        filters = Q(user=self.request.user)
        return Record.objects.filter(filters)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CauseDonation(generics.ListAPIView):
    serializer_class = CauseDonationSerializer

    def get_queryset(self):
        search_term = self.request.query_params.get("cause")
        return Record.objects.filter(
            cause__icontains=search_term, user=self.request.user
        )
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




