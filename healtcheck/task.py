from celery import shared_task
from time import sleep
import os
import csv
import json
from django.template.loader import render_to_string
import requests
from django.conf import settings
from requests.api import request


@shared_task
def celfir(timecap):
    print("------------Print Before -------------------")
    sleep(timecap)
    print("------------Print After Sleeping 2 Secound -------------------")
    return None
