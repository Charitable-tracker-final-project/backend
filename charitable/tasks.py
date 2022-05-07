from charitable_tracker.celery import Celery, app
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from charitable_tracker import settings
from celery import Celery
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask
from .models import EmailReminder

@app.task
def test_email():
    crontab(minute='*/5')
    send_mail(
                subject=('Friendly Reminder from Charitable Tracker'),
                message=(f'Hi jocelyn. this is a test.'),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['inlay.j@gmail.com']
                )

@app.task
def mail_create(reminder_pk):
    reminder = EmailReminder.objects.get(pk=reminder_pk)
    send_mail(
                subject=('Friendly Reminder from Charitable Tracker'),
                message=(f'Hi {reminder.user}. {reminder.message}.'),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[reminder.email]
                )
    if reminder.interval == 'Weekly' and reminder.subscribe == True:
            crontab(0,0, day_of_week='sun')
    elif reminder.interval == 'BiWeekly' and reminder.subscribe == True:
            crontab(0,0, day_of_month='1,15')
    elif reminder.interval == 'Monthly' and reminder.subscribe == True:    
            crontab(0,0, day_of_month='1')
    elif reminder.interval == 'Yearly' and reminder.subscribe == True:
            crontab(0,0, month_of_year='5')