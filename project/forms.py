#-*-coding: utf-8 -*-
from django import forms
from models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ('title', 'text', 'leader', 'logo')