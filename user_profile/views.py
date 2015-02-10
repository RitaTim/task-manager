#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from user_profile.forms import UserProfileForm 
from user_profile.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from project.models import Project
from task.models import Task

@login_required
def profile(request, id_project = 0):
	if request.method == "POST":
		form = UserProfileForm(request.POST, instance = request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('/profile')
		return HttpResponse('форма не валидна')

	user = request.user
	profile = user.profile
	#form_profile = UserProfileForm(instance = profile)
	#form_user = UserForm(request.POST)
	args = {}
	args.update(csrf(request))

	args['profile'] = profile
	args['user'] = user
	args['projects'] = Project.objects.all()
	return render_to_response('profile.html', args)

def dashboard(request, id_project = 0):
	user = request.user
	args = {}
	args.update(csrf(request))
	args['user'] = user
	if id_project != 0:
		args['tasks'] = Task.objects.filter(assigned = user.id, project = id_project)
	else:
		args['tasks'] = Task.objects.filter(assigned = user.id)
	args['projects'] = Project.objects.all()
	if id_project != 0:
		args['project'] = Project.objects.get(id = id_project)
	return render_to_response('dashboard.html', args)

def dashboard_change():
	return
