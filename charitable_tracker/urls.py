"""charitable_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from charitable import views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/Dgoals/", cviews.DonationGoalListView.as_view()),
    path("api/Dgoal/<int:pk>/", cviews.DonationGoalDetailView.as_view()),
    path("api/Vgoals/", cviews.VolunteerGoalListView.as_view()),
    path("api/Vgoal/<int:pk>/", cviews.VolunteerGoalDetailView.as_view()),
    path("api/Drecords/", cviews.DonationRecordListView.as_view()),
    path("api/Drecord/<int:pk>/", cviews.DonationRecordDetailView.as_view()),
    path("api/Vrecords/", cviews.VolunteerRecordListView.as_view()),
    path("api/Vrecord/<int:pk>/", cviews.VolunteerRecordDetailView.as_view()),
    path("api/Dbreakdown/<int:pk>/", cviews.DonationGoalBreakdownView.as_view()),
    path("api/annualincome/", cviews.AnnualIncomeView.as_view()), 
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]
