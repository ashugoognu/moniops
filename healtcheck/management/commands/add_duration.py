from django.core.management.base import BaseCommand, CommandError
from datetime import datetime,timedelta
from django.utils import timezone
import pytz


class Command(BaseCommand):
    help = 'Geting all batch recording data'

    def handle(self, *args, **kwargs):
                