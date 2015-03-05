# -*- coding: utf-8 -*-
from django.contrib import admin
from comment.models import Comment 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('updated', 'text')

admin.site.register(Comment, CommentAdmin)
