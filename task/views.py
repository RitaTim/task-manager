#-*-coding: utf-8 -*-
#from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from task.models import Task
from project.models import Project
from forms import TaskForm
from iteration.models import Iteration
from django.contrib.auth.models import User
import json
import logging

def new(request, id_project = 0):
	user = request.user
	project = Project.objects.get(id = id_project)	
	entr = user.id
	pro = project.id

	if request.method == "POST":
		form = TaskForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/projects")
		return HttpResponse("Форма не валидна")

	args = {}
	args.update(csrf(request))
	args['user'] = user
	args['form'] = TaskForm(project = pro, entrasted = entr)
	args['project']	= project
	return render_to_response('new_task.html', args)

def show_tasks(request, id_project = 0, sort_by = "sort_by_update"):
	if request.GET:
		return HttpResponse(request)

	user = request.user

	args = {}
	args['user'] = user
	args['projects'] = Project.objects.all() 
	if sort_by == "sort_by_title":
		args['tasks'] = Task.objects.filter(project = id_project).order_by('title')
	elif sort_by == "sort_by_iterate":
		args['tasks'] = Task.objects.filter(project = id_project).order_by('iterate')
	elif sort_by == "sort_by_type":
		args['tasks'] = Task.objects.filter(project = id_project).order_by('type_task')
	elif sort_by == "sort_by_assigned":
		args['tasks'] = Task.objects.filter(project = id_project).order_by('assigned')
	elif sort_by == "sort_by_status":
		args['tasks'] = Task.objects.filter(project = id_project).order_by('status')
	else:
		args['tasks'] = Task.objects.filter(project = id_project).order_by('updated')
	args['project'] = Project.objects.get(id = id_project)

	try:
		args['iterations'] = Iteration.objects.filter(project = id_project)
	except Iteration.DoesNotExist:
		args['iterations'] = []

	i = 12
	for task in args['tasks']:
		task.pos = i
		i -= 3
		logging.info(task.id)

	return render_to_response('tasks.html', args)

def change_order(request, id_project = 1):
	args = "{'id': " + request.GET['id'] + ", 'fromPosition' : " + request.GET['fromPosition'] + ", 'toPosition' : " + request.GET['toPosition'] + ", 'direction' : " + request.GET['direction'] + "}"
	#args = request.GET
	return HttpResponse(args) #json.dumps(args))

def show_dashboard(request, id_project="", id_iteration="", id_user=""):
	user = request.user
	args = {}
	args.update(csrf(request))
	args['user'] = user	

	args['projects'] = Project.objects.all()
	if id_project != -1:
		args['project'] = Project.objects.get(id = id_project)
		try:
			args['iterations'] = Iteration.objects.filter(project = id_project).order_by('dead_line')
		except Iteration.DoesNotExist:
			args['iterations'] = []
	return render_to_response('dashboard.html', args)

def get_tasks(request, title_project="", title_iteration="", name_task=""):
	logging.info("in get_tasks")
	if request.method == 'GET':
		#title_project 	= request.GET['title_project']
		#title_iteration = request.GET['title_iteration']
		#name_user 		= request.GET['name_user']
    
		#if title_project != "":
		#	id_project = Project.objects.get(title = title_project).id
		#	tasks = Task.objects.filter(project = id_project)
		#else:
		#	tasks = Task.objects.filter()
		#
		#if title_iteration != "":
		#	id_iteration = Iteration.objects.get(title = title_iteration).id
			
		#if name_task == "мои":
		#	id_user = request.user.id

		#for task in tasks:
		#	if (id_iteration and task.iterate != id_iteration) or (id_user and task.user != id_user):
		#		task.delete()

		tasks_to_do 		= []
		tasks_in_progress 	= []
		tasks_test			= []
		tasks_done			= []
		tasks_not_dev		= []

		#for task in tasks:
		#	if task.status   == "not_dev":
		#		tasks_not_dev.push(task)
		#	elif task.status ==	"to_do":	
		#		tasks_to_do.push(task)
		#	elif task.status == "in_progress":
		#		tasks_in_progress.push(task)
		#	elif task.status == "test":
		#		tasks_test.push(task)
		#	elif task.status == "done":
		#		tasks_done.push(task)

	return json.dumps("{'tasks_not_dev' : tasks_not_dev, 'tasks_in_progress' : tasks_in_progress, 'tasks_test' : tasks_test,  'tasks_done' : tasks_done,  'tasks_to_do' : tasks_to_do}")
