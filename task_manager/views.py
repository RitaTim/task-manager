#-*-coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from iteration.models import Iteration
from project.models import Project
from task.models import Task

import logging

def show_project(request, id_project = 0):
	if request.GET:
		return HttpResponse(request)

	args = {}
	args['user'    ] = request.user
	args['projects'] = Project.objects.exclude(id=id_project)
	args['project' ] = Project.objects.get(id = id_project)
	args['tasks'   ] = Task.objects.filter(project = id_project)	

	try:
		args['iterations'] = Iteration.objects.filter(project = id_project)
	except Iteration.DoesNotExist:
		args['iterations'] = []

	return render_to_response('main.html', args)
