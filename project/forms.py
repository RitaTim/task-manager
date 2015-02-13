#-*-coding: utf-8 -*-
from django import forms
from models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ('title', 'text', 'leader', 'logo')

	# def save(self, commit = True):
	# 	#if self.cleaned_data['name_leader']:
	# 		#leader = User.objects.get(username = self.fields['name_leader'])
	# 		#self.fields['leader_id'] = leader.id

	# 	project = super(ProjectForm, self).save(commit = False)

	# 	if commit:
	# 		project.save()

	# 	return project
