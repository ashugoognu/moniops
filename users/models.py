from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext_lazy as _


class CustomUserModel(AbstractUser):
    USER_TYPE = (
        ('admin','Admin'),
        ('customer','Customer'),
    )
    exist_employee = models.BooleanField(default=True)
    mobile = models.CharField(max_length=12,blank=True)
    user_type = models.CharField(max_length=25,choices=USER_TYPE,default='admin')
    is_verified = models.BooleanField(default = True, null=True)
    @property
    def name(self):
        return self.get_full_name()