# -*- coding: utf-8 -*-
from django.contrib import admin
from forum.models import Forum 

class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Forum, ForumAdmin)
