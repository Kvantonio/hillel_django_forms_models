from celery import shared_task

from django.core.mail import send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def send_date_reminder(email, rem_text):
    send_mail(
        'From my past',
        rem_text,
        email,
        [email],
    )
