#-*-coding: utf-8 -*-
from django import forms
from models import Task

class TaskForm(forms.ModelForm):
	
	class Meta:
		model = Task
		fields = ('title', 'type_task', 'text', 'assigned', 'priority', 'iterate', 'dead_line','main_task', 'project', 'entrasted')

	def __init__(self, *args, **kwargs):
		#t = False
		if kwargs:
			self.project = kwargs.pop('project')
			self.entrasted = kwargs.pop('entrasted')
		super(TaskForm, self).__init__(*args, **kwargs)
		#if kwargs:
		#	self.fields['project'].initial = kwargs.pop('project', 0)
		#	self.fields['entrasted'].initial = kwargs.pop('entrasted', 0)	
		

	def save(self, commit = True):
		#if self.cleaned_data['name_leader']:
			#leader = User.objects.get(username = self.fields['name_leader'])
			#self.fields['leader_id'] = leader.id
		task = super(TaskForm, self).save(commit = False)

		if commit:
			task.save()

		return task


