from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Job



@shared_task
def email_apply(request,slug):
    job = Job.objects.get(slug=slug)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = f'Hi, {name} '
        full_message = f'your Applyed on {job} in JobBoard.com '
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )