#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from project.models import Project
from iteration.models import Iteration
from forms import ProjectForm
from django.contrib.auth.models import User
import logging
from django.core.cache import cache
from datetime import datetime

def edit_project(request):
	project_id = cache.get('project_id')
	if request.method == "POST":
		if project_id:
			project = Project.objects.get(id = project_id) 
			form 	= ProjectForm(request.POST, instance = project)
		else:
			form = ProjectForm(request.POST, request.FILES)

		if not form.is_valid():
			return HttpResponse("Форма не валидна")
		
		form.save()	

		return redirect(request.META.get('HTTP_REFERER','/'))
	else: # GET
		args={}
		args.update(csrf(request))

		if project_id:
			project = Project.objects.get(id = project_id)
			args['form'] = ProjectForm(instance = project)
			args['project'] = Project.objects.get(id = project_id)
		else:
			args['form'] = ProjectForm()		

		return render_to_response('project_edit.html', args)

def projects(request):
	user_name = request.user.username
	cache.delete_many( [ 'project_id', 'iterate_id' ])
	cache.set_many( { 'user_id' : request.user.id, 'user_name' : user_name })
	logging.info(cache.get('user_name'))

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
	args['project']   = Project.objects.filter(id = project_id).values('title', 'text', 'logo', 'leader__username')[0]
	cache.set('project_title', args['project']['title'])
	
	args['iterations'] = Iteration.objects.filter(project_id = project_id).values('id', 'title')
	if args['iterations']:
		today_time  = datetime.now
		cur_iterate = Iteration.objects.filter( dead_line__gt = today_time, start_line__lt = today_time )[0].id
		cache.set('iterate_id', cur_iterate)

	logging.info(cache.get('user_name'))
	args['cache'] = { 'user_name' : cache.get('user_name') }
	return render_to_response('project.html', args)
