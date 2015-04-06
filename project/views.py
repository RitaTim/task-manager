#-*-coding: utf-8 -*-
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from task_manager.utils             import get_current_iterate
from django.shortcuts               import render_to_response, redirect
from django.http.response           import HttpResponse, Http404
from iteration.models  import Iteration
from task.models       import Task
from models            import Project
from forms             import ProjectForm
from django.core.cache import cache
from datetime          import datetime
import logging

def edit_project(request):	
	if request.method == "POST":
		project_id = cache.get('project_id')
		cache.set('test', request.FILES)
		if project_id:
			project = Project.objects.get(id = project_id) 
			form 	= ProjectForm(request.POST, request.FILES, instance = project)
		else:
			form = ProjectForm(request.POST, request.FILES)

		if not form.is_valid():
			return HttpResponse("Форма не валидна")
		
		form.save()	

		return redirect(request.META.get('HTTP_REFERER','/'))
	else: # GET
		args={}
		args.update(csrf(request))

		if 'project_id' in request.GET:
			project_id = request.GET['project_id']
			project = Project.objects.get(id = project_id)
			args['form'] = ProjectForm(instance = project)
			args['project'] = Project.objects.get(id = project_id)
		else:
			args['form'] = ProjectForm()		

		return render_to_response('project_edit.html', args)

@login_required
def projects(request):
	user_name = request.user.username
	cache.delete_many( [ 'project_id', 'iterate_id' ])
	cache.set_many( { 'user_id' : request.user.id, 'user_name' : user_name })

	args = {}
	args['projects'] = Project.objects.all().values('id', 'title', 'logo', 'text')
	args['cache'] = { 'user_name' : user_name }

	return render_to_response('projects.html', args)

def show_project(request):
	if 'project_id' in request.GET:
		project_id = request.GET['project_id']
		cache.set('project_id', project_id)
	else:
		project_id = cache.get('project_id')
	
	args = {}
	args['project']   = Project.objects.filter(id = project_id).values('id', 'title', 'text', 'logo', 'leader__username')[0]
	cache.set('project_title', args['project']['title'])
	
	args['iterations'] = Iteration.objects.filter(project_id = project_id).values('id', 'title')
	
	cur_iterate = get_current_iterate(project_id)
	cache.set('iterate_id', cur_iterate)
	args['iterate_title'] = Iteration.objects.filter(id = cur_iterate).values('title')[0]['title']

	args['new_tasks'] = Task.objects.filter(project = project_id).values('title', 'id', 'entrasted__username', 'assigned__username', 'type_task') .order_by('-updated')[0:5]

	args['cache'] = { 'user_name' : cache.get('user_name') }
	return render_to_response('project.html', args)