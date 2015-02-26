#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from user_profile.forms import UserProfileForm 
from user_profile.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from iteration.models import Iteration
from project.models import Project
from task.models import Task
import json
import logging
#from django.http import JsonResponse

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

	args = {}
	args.update(csrf(request))

	args['projects'] = Project.objects.exclude(id=id_project)
	try:
		args['iterations'] = Iteration.objects.filter(project = id_project)
	except Iteration.DoesNotExist:
		args['iterations'] = []
		
	args['profile'] = profile
	args['user'] = user
	tasks = Task.objects.filter(assigned = user.id).exclude(status="not_dev")
	tasks_to_do        = tasks.filter( status="to_do"       ).values('title', 'id')
	tasks_in_progress  = tasks.filter( status="in_progress" ).values('title', 'id')
	tasks_test         = tasks.filter( status="test"        ).values('title', 'id')
	tasks_done         = tasks.filter( status="done"        ).values('title', 'id')
	args['type_tasks'] = [ tasks_to_do, tasks_in_progress, tasks_test, tasks_done]
	return render_to_response('profile.html', args)

def get_task(request, id_task = 0):
	task = Task.objects.get(id = id_task)
	data = { 'title': task.title, 'text': task.text }
	return HttpResponse(json.dumps(data), content_type='application/json')
