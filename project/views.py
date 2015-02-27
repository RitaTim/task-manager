#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from project.models import Project
from iteration.models import Iteration
from forms import ProjectForm
from django.contrib.auth.models import User
import logging

def edit_project(request, id_project = '0'):
	if request.method == "POST":
		if id_project != '0':
			project = Project.objects.get(id = id_project) 
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

		if 'id_project' in request.GET:
			id_project = request.GET['id_project']
		if id_project != '0':
			project = Project.objects.get(id = id_project)
			args['form'] = ProjectForm(instance = project)
			args['project'] = Project.objects.get(id = id_project)
		else:
			args['form'] = ProjectForm()
		

		return render_to_response('project_edit.html', args)

def projects(request):
	user = request.user
	
	args = {}
	args['user'] = user
	args['projects'] = Project.objects.all() 
	if 'filter' in request.GET:
		args['filter'] = request.GET['filter']
	else:
		args['filter'] = 0

	return render_to_response('projects.html', args)

def show_project(request, id_project = 0):
	user = request.user

	args = {}
	args['user'] = user
	args['projects'] = Project.objects.values('id', 'title')
	args['project'] = Project.objects.get(id = id_project)
	args['iterations'] = Iteration.objects.filter(project_id = id_project).values('id', 'title')
	return render_to_response('project.html', args)
