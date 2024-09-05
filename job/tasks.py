from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task
from .models import Job

@shared_task
def email_apply(request, slug):
    job = Job.objects.get(slug=slug)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = f'Application Confirmation - {job.title}'

        full_message = f"""
        Dear {name},

        Thank you for applying to the {job.title} position at JobBoard.com.

        We have successfully received your application and we will review it shortly. 
        You applied for the following job:

        Job Title: {job.title}
        Job Description: {job.description}
        Location: {job.country}

        If your profile matches the job requirements, our team will contact you for the next steps.

        We wish you the best of luck in your job search!

        Kind regards,
        JobBoard Team
        """

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
