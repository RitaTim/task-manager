# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class UserForm(forms.ModelForm):
	
    class Meta:
        model = User
        fields = ( 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ( 'avatar', 'date_of_birth', 'level',)

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ( 'date_of_birth', 'phone', 'avatar')

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ( 'username', 'first_name', 'last_name', 'email')