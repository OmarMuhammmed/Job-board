from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from .models import Info

def send_message(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            user_email = form.cleaned_data['email']  
            message = form.cleaned_data['message']

          
            email_message = EmailMessage(
                subject,
                message,
                user_email,  # from 
                [settings.EMAIL_HOST_USER], # To   
            )

            
            email_message.send()

            messages.success(request, 'Sending Message Successfully..')

    else:
        form = ContactForm()

    context = {
        'info': Info.objects.get(),
        'form': form
    }

    return render(request, 'contact/contact.html', context)
