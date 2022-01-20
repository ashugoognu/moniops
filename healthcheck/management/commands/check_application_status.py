from django.core.management.base import BaseCommand, CommandError
from datetime import datetime,timedelta
from django.utils import timezone
import pytz
from healthcheck.views import check_application_status
from projects.models import Projects,Applications
from background_task import background

class Command(BaseCommand):
    help = 'Get all the application and check status...'

    def handle(self, *args, **kwargs):
        application_obj = Applications.objects.all()
        print("-----------------")
        for i in application_obj:
            if i.frequency:
                check_application_status(i.id,schedule=timedelta(minutes=i.frequency))
                print(i.id)