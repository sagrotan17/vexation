from django.core.mail import EmailMessage, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactForm




def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']


            try:
                email = EmailMessage( subject, message, from_email, ['nobody@example.com'], reply_to=["dorian@vexation.de"],)
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('./success/')

    return render(request, "contact/email.html", {'form': form})


def successView(request):
    return render(request, "contact/success.html",)