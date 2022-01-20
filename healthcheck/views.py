from django.shortcuts import render
from datetime import timedelta
from projects.models import Projects,Applications
from background_task import background
import urllib.request
from django.http import JsonResponse

# Create your views here.

def create_task(request):
    return jsonResponse("ok")

@background()
def check_application_status(application_id):
    print("Check for the application id is:", application_id)
    application_queryset = Applications.objects.filter(id=application_id).first()
    application_url = application_queryset.url

    site_status = urllib.request.urlopen(application_url).getcode()
    print("Status is: ", site_status)
    if site_status==200:
        print("Site is up...")
    else:
        print("Site is Down...")