from django.shortcuts import render
from datetime import timedelta
from projects.models import Projects,Applications
from background_task import background
import urllib.request
from django.http import HttpResponse, JsonResponse

# Create your views here.

def create_task(request):
    run_cron_job(repeat=60)
    return HttpResponse("ok")

@background()
def run_cron_job():
    application_obj = Applications.objects.all()
    print("########## Adding Task to Queue ##########")
    for i in application_obj:
        if i.frequency:
            check_application_status(i.id,schedule=timedelta(minutes=i.frequency))
            print(i.id," Adding ", i.name, ". Checking for URL : ", i.url)

    

@background()
def check_application_status(application_id):
    
    application_queryset = Applications.objects.filter(id=application_id).first()
    print("Application id is : ",application_id,"Check for the application : ", application_queryset.name, "URL is : ", application_queryset.url )
    application_url = application_queryset.url
    site_status = None
    try:
        site_status = urllib.request.urlopen(application_url).getcode()
    except Exception as e:
        print(e)
        print("********* ALERT ********************")
        print("May be problem with application name : ", application_queryset.name, "URL is : ", application_queryset.url)
    if site_status:
        if site_status==200:
            print("Status is: ", site_status," Site is up...URL is :", application_queryset.url)
        else:
            print("Status is: ", site_status, " Site is Down...URL is :", application_queryset.url)
    else:
            print("Status is: ", site_status, " Site is Down...URL is :", application_queryset.url)