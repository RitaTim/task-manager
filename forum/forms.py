#-*-coding: utf-8 -*-
from django import forms
from models import Forum

class ForumForm(forms.ModelForm):
	
	class Meta:
		model = Forum
		fields = ('title', 'project')