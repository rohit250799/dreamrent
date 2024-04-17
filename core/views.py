import logging #importing the logging library
import datetime
from django.shortcuts import render
from django.http import HttpResponse

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
