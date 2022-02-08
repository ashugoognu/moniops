from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey
from users.models import CustomUserModel

# from healthcheck.task import *

# Create your models here.

class NotificationSubscriber(models.Model):
    # user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True)
    subscriber_name = models.CharField(max_length=250, null=False, blank=False, default=None)
    subscriber_mobile =  models.CharField(max_length=250, null=False, blank=False, default=None)
    subscriber_email =  models.CharField(max_length=250, null=False, blank=False, default=None)
    email = models.BooleanField(default=False,help_text="Check if you want to send alert on Email.")
    sms = models.BooleanField(default=False,help_text="Check if you want to send alert on SMS.")
    call = models.BooleanField(default=False,help_text="Check if you want to send alert on Call.")

    def __str__(self):
        return "{0}-(Email: {1}, SMS: {2}, Call: {3})".format(self.subscriber_name,str(self.email),str(self.sms),str(self.call))

class NotificationGroup(models.Model):
    group_name = models.CharField(max_length=250, null=False, blank=False, default=None)
    group = models.ManyToManyField(NotificationSubscriber)

    def __str__(self):
        return self.group_name

class Projects(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250, null=False, blank= False)
    description = models.TextField(null=True, blank= True)
    notification_group = models.ForeignKey(NotificationGroup,null=True, blank=False, default=None,on_delete=SET_NULL)

    def __str__(self):
        return "{0} - ({1})".format(self.name, self.user)

class Applications(models.Model):
    project = models.ForeignKey(Projects,on_delete=SET_NULL,null=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    frequency = models.IntegerField(default=1)

