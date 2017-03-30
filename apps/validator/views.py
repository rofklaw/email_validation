from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, 'validator/index.html')

def register (request):
    user_email = Email.objects.validmail(request.POST['email'])
    if user_email['errors'] != []:
        for errors in user_email['errors']:
            print errors
            messages.add_message(request, messages.ERROR, errors)
            return redirect('/')

    Email.objects.create(email = request.POST['email'])
    request.session['email'] = request.POST['email']
    context = {
    'contents': Email.objects.all()
    }
    # print contents
    return render(request, 'validator/success.html', context)
