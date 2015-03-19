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
from user_profile.models import UserProfile
import json
import logging
from datetime import datetime
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from django.core.cache import cache
#from django.http import JsonResponse

@login_required
def profile(request, id_project = 0):
	if request.method == "POST":
		form = UserProfileForm(request.POST, instance = request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('/profile')
		return HttpResponse('форма не валидна')

	args = {}
	args.update(csrf(request))
	args['cache']   = cache.get_many( [ 'user_id', 'project_id', 'iterate_id', 'project_title', 'user_name' ] )		
	args['user']    = UserProfile.objects.filter(id = args['cache']['user_id']).values('id', 'user__username', 'user__first_name', 'user__last_name', 'level', 'avatar', 'date_of_birth')
	args['project'] = Project.objects.filter( id = args['cache']['project_id'] ).values('title')[0]
	
	tasks = Task.objects.filter(assigned = args['cache']['user_id'], project = args['cache']['project_id'] ).exclude(status="not_dev")
	args['type_tasks'] = [ 'tasks_to_do', 'tasks_in_progress', 'tasks_test', 'tasks_done']

	if args['project']:
		args['iterate_curr_id'] = args['cache']['iterate_id']	
		try:
			args['iterates'] = Iteration.objects.filter(project = args['cache']['project_id'] )
		except Iteration.DoesNotExist:
			args['iterates'] = []
		
	return render_to_response('profile.html', args)

def get_tasks(request, id_iterate = 0):
	today_time = datetime.now
	tasks   = Task.objects.filter(assigned = request.user.id, iterate = id_iterate).exclude(status="not_dev")

	tasks_to_do 		= []
	tasks_in_progress 	= []
	tasks_test			= []
	tasks_done			= []
	
	tasks = tasks.values('id', 'title', 'status') if tasks else []
	for task in tasks:
	 	if  task['status'] == "to_do":	
			tasks_to_do.append(task)
		elif task['status'] == "test":
			tasks_test.append(task)
		elif task['status'] == "in_progress":
			tasks_in_progress.append(task)
		elif task['status'] == "done":
			tasks_done.append(task)

	data = { 'tasks' : {'tasks_to_do' : tasks_to_do, 'tasks_in_progress' : tasks_in_progress, 'tasks_test' : tasks_test, 'tasks_done' : tasks_done} }
	return HttpResponse(json.dumps(data), content_type='application/json')

def get_task(request, id_task = 0):
	task = Task.objects.get(id = id_task)
	data = { 'title': task.title, 'text': task.text }
	return HttpResponse(json.dumps(data), content_type='application/json')