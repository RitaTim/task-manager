# -*- coding: utf-8 -*-
from django.contrib import admin
from iteration.models import Iteration 

class IterationAdmin(admin.ModelAdmin):
    list_display = ('title', 'dead_line',)

admin.site.register(Iteration, IterationAdmin)