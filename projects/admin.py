from django.contrib import admin

# Register your models here.

from . models import Projects,Applications,NotificationSubscriber,NotificationGroup

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id','name','user','notification_group']
admin.site.register(Projects,ProjectsAdmin)

class Applicationsadmin(admin.ModelAdmin):
    list_display = ['id','project','name','url','frequency']
admin.site.register(Applications,Applicationsadmin)

class NotificationSubscriberAdmin(admin.ModelAdmin):
    list_display = ['id','subscriber_name','subscriber_email','subscriber_mobile','email','sms','call']
admin.site.register(NotificationSubscriber,NotificationSubscriberAdmin)

class NotificationGroupAdmin(admin.ModelAdmin):
    list_display = ['id','group_name',]
admin.site.register(NotificationGroup,NotificationGroupAdmin)