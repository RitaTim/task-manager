# -*- coding: utf-8 -*-
from django.contrib import admin
from user_profile.models import UserProfile 

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'date_of_birth', 'avatar',)

    def get_username(self, instance):
        # instance is User instance
        return instance.user.username

admin.site.register(UserProfile, UserProfileAdmin)