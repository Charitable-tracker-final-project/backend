from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets, filters, status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import User, Profile, Donationrecord, Volunteerrecord, Volunteergoal, Donationgoal
from .serializers import DonationGoalsSerializers, VolunteerGoalsSerializers, DonationRecordSerializers, VolunteerRecordSerializers, DonationGoalBreakdownSerializer, ProfileSerializer
from django.db.models import Q


class DonationGoalListView(generics.ListCreateAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerGoalListView(generics.ListCreateAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerGoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteergoal.objects.all()
    serializer_class = VolunteerGoalsSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationRecordListView(generics.ListCreateAPIView):
    queryset = Donationrecord.objects.all()
    serializer_class = DonationRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly 

class DonationRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donationrecord.objects.all()
    serializer_class = DonationRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class VolunteerRecordListView(generics.ListCreateAPIView):
    queryset = Volunteerrecord.objects.all()
    serializer_class = VolunteerRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly 

class VolunteerRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Volunteerrecord.objects.all()
    serializer_class = VolunteerRecordSerializers
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class DonationGoalBreakdownView(generics.ListCreateAPIView):
    queryset = Donationgoal.objects.all()
    serializer_class = DonationGoalBreakdownSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly

class AnnualIncomeView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()    
    serializer_class = ProfileSerializer
    permissions_classes = permissions.IsAuthenticatedOrReadOnly