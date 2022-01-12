from django.contrib import admin

# Register your models here.

from . models import Projects,Applications

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Projects,ProjectsAdmin)

class Applicationsadmin(admin.ModelAdmin):
    list_display = ['id','project','name','url','frequency']
admin.site.register(Applications,Applicationsadmin)