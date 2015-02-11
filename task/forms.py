#-*-coding: utf-8 -*-
from django import forms
from models import Task

class TaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = ('title', 'type_task', 'text', 'assigned', 'priority', 'iterate', 'dead_line','main_task', 'project', 'entrasted')


