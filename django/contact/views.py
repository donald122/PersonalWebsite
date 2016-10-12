from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.template import Context
from django.core.validators import validate_email
from home.models import QuotesContainer
from django.db import models


def contact(request):

    is_sent = False
    quote_container_object_list = QuotesContainer.objects.live()

    # need the page dictionary, because base template using wagtail model tag which start with page. eg page.quote_container_object_list.0.object
    page = {
        'quote_container_object_list': quote_container_object_list
    }

    if request.method == 'POST':



        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        try:
            validate_email(email)
        except forms.ValidationError:
            return redirect('contact')

        if firstname and lastname and email and content:            

            # Email the profile with the 
            # contact information
            mailtemplate = loader.get_template('contact/mail_template.txt')
            mailcontext = Context({
                'contact_firstname': firstname,
                'contact_lastname': lastname,
                'contact_email': email,
                'form_content': content,
            })
            mailcontent = mailtemplate.render(mailcontext)

            try:
                send_mail(
                    'New contact form submission',
                    mailcontent,
                    'donald.leung@icloud.com',
                    ['donald.leung@icloud.com'],
                    fail_silently=False,
                )
            except BadHeaderError:
                return redirect('contact')

            is_sent = True
            context = {         
                'is_sent': is_sent,
                'page': page
            }

            return render(request, 'contact/contact_page.html', context = context)


    context = {
        'is_sent': is_sent,
        'page': page
    }

    return render(request, 'contact/contact_page.html', context = context)
# Create your views here.
