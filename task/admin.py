# -*- coding: utf-8 -*-
from django.contrib import admin
from task.models import Task 

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'type_task', 'assigned', 'entrasted', 'iterate')

admin.site.register(Task, TaskAdmin)