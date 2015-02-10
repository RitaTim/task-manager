# -*- coding: utf-8 -*-
from django.contrib import admin
from project.models import Project 

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'leader',)

admin.site.register(Project, ProjectAdmin)
    
