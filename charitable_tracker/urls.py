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
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("api/Dgoals/", cviews.DonationGoalListView.as_view()),
    path("api/Dgoal/<int:pk>/", cviews.DonationGoalDetailView.as_view()),
    path("api/Vgoals/", cviews.VolunteerGoalListView.as_view()),
    path("api/Vgoal/<int:pk>/", cviews.VolunteerGoalDetailView.as_view()),
    path("api/Drecords/", cviews.DonationRecordListView.as_view()),
    path("api/Drecord/<int:pk>/", cviews.DonationRecordDetailView.as_view()),
    path("api/Vrecords/", cviews.VolunteerRecordListView.as_view()),
    path("api/Vrecord/<int:pk>/", cviews.VolunteerRecordDetailView.as_view()),
    path("api/Dbreakdown/<int:pk>/", cviews.DonationGoalBreakdownView.as_view()),
    path("api/Vbreakdown/<int:pk>/", cviews.VolunteerGoalBreakdownView.as_view()),
    path("api/organizationdonation/", cviews.OrganizationDonation.as_view()),
    path("api/organizationtime/", cviews.OrganizationTime.as_view()),
    path("api/causedonation/", cviews.CauseDonation.as_view()),
    path("api/causetime/", cviews.CauseTime.as_view()),
    path("api/annualincome/", cviews.AnnualIncomeView.as_view()),
    path("api/upload/", cviews.DocumentCreateView.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/reminders/', cviews.EmailReminderView.as_view()),
    path('api/reminder/<int:pk>/', cviews.EmailReminderDetailView.as_view()),
    path('auth/google/', cviews.GoogleLogin.as_view(), name='google_login'),
    path('api/Dsort/', cviews.DonationAllGoalRecordListView.as_view()),
    path('api/Vsort/', cviews.VolunteerAllGoalRecordListView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
