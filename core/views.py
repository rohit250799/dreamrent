import logging #importing the logging library
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)  #getting an instance of the logger

# Create your views here.
def frontpage(request):
    return render(request, 'core/frontpage.html') 

def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            account_type = request.POST.get('account_type', 'buyer')
            if account_type == 'seller':
                userprofile = Userprofile.objects.create(user=user, is_seller=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)
            return HttpResponse("dashboard")
    else:
        form = UserCreationForm()
    return render(request, 'user_authentication/signup.html', {
        'form': form,
    })

def dashboard(request):
    return render(request, 'core/dashboard.html', {
        'userprofile': request.user.userprofile,
    })

def hello_reader(request):
    logger.warning('Homepage was accessed at '+str(datetime.datetime.now())+' hours!')
    return HttpResponse("<h1>Hello FreeCodeCamp.org Reader :)</h1>")


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'Logged out succesfully')
    return render(request, 'core/login.html')

class HelloView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, reequest):
        content = {'message': 'Hello Rohit'}
        return Response(content)
