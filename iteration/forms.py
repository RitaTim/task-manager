#-*-coding: utf-8 -*-
from django import forms
from models import Iteration

class IterationForm(forms.ModelForm):
	
	class Meta:
		model = Iteration
		fields = ('title', 'start_line', 'dead_line', 'project')


