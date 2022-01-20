from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields.related import ForeignKey
from users.models import CustomUserModel

# from healthcheck.task import *

# Create your models here.

class Projects(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250, null=False, blank= False)
    description = models.TextField(null=True, blank= True)

    def __str__(self):
        return "{0} - ({1})".format(self.name, self.user)

class Applications(models.Model):
    project = models.ForeignKey(Projects,on_delete=SET_NULL,null=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    url = models.CharField(max_length=250, null=True, blank=True)
    frequency = models.IntegerField(default=1)