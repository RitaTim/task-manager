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
from django.db.models import Q
#from django.http import JsonResponse

@login_required
def profile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST, instance = request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('/profile')
		return HttpResponse('форма не валидна')

	data_projects = _get_data_projects(request)

	args = {}
	args.update(csrf(request))
	args['cache']   = cache.get_many( [ 'user_id', 'project_id', 'project_title', 'user_name', 'iterate_id' ] )
	
	if 'empty' in data_projects:
		args['empty'] = data_projects['empty']
		return render_to_response('profile.html', args)

	args['user']    = UserProfile.objects.filter(id = args['cache']['user_id']).values('id', 'user__username', 'user__first_name', 'user__last_name', 'level', 'avatar', 'date_of_birth')
	args['projects']   = data_projects['projects']
	args['iterates']   = data_projects['iterates']
	args['iterate_id'] = data_projects['iterate_id']
	args['project']    = Project.objects.filter( id = data_projects['project_id'] ).values('title')[0]
	
	tasks = Task.objects.filter(assigned = args['cache']['user_id'], project = data_projects['project_id'] ).exclude(status="not_dev")
	
	args['type_tasks'] = [ 'tasks_to_do', 'tasks_in_progress', 'tasks_test', 'tasks_done']
	
	return render_to_response('profile.html', args)

def get_tasks(request, iterate_id = 0):
	today_time = datetime.now

	user_id = cache.get('user_id')
	tasks   = Task.objects.filter(assigned = user_id, iterate = iterate_id).exclude(status="not_dev")

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

def _get_data_projects(request):
	user_id = cache.get('user_id')
	projects_id = Task.objects.filter( Q(assigned = user_id) | Q(entrasted = user_id) ).exclude( project = None ).order_by('updated').values('project__id').distinct()
	projects    = Project.objects.filter( id__in = projects_id ).values('id', 'title')
	data_cache = cache.get_many([ 'project_id', 'iterate_id' ])

	if not projects:	
		if not data_cache:
			return { 'empty' : 'all' }
		else:
			return { 'empty' : 'user' }
	else:
		if data_cache:
			if data_cache['project_id'] in projects:
				project_id = data_cache['project_id']
				iterate_id = data_cache['iterate_id']
			else:
				project_id = projects[0]['id']
				iterate_id = _get_current_iterate_project(request, project_id)
		else:
			project_id = projects[0]['id']			
			iterate_id = _get_current_iterate_project(request, project_id)
			cache.set_many( { 
				'project_id'   : project_id,
				'project_title': projects[0]['title'],
				'iterate_id'   : iterate_id
			} )

	iterates = Iteration.objects.filter( project = project_id ).values('id', 'title')	

	return { 
		'projects'   : projects,
		'project_id' : project_id,
		'iterates'   : iterates,
		'iterate_id' : iterate_id,
	}

def _get_current_iterate_project(request, project_id = 0):
	today_time  = datetime.now
	try:
		curr_iterate = Iteration.objects.filter( project = project_id, dead_line__gt = today_time, start_line__lt = today_time).order_by('-dead_line')[0].id
		return curr_iterate
	except Iteration.DoesNotExist:
		return 0


def change_iterates(request, project_id = 0):
	iterates_  = Iteration.objects.filter(project = project_id).values('id', 'title')
	iterates   = []
	for iterate in iterates_:
	 	iterates.append(iterate)
	iterate_id = _get_current_iterate_project(request, project_id)
	return HttpResponse(json.dumps({
		'iterates'   : iterates,
		'iterate_id' : iterate_id
	}), content_type='application/json')