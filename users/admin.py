from django.contrib import admin

# Register your models here.
from .models import CustomUserModel

class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','email','mobile','user_type','is_active']
admin.site.register(CustomUserModel,CustomUserModelAdmin)