#-*-coding: utf-8 -*-
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

def show_tasks(request, id_project = 0):
	if request.GET:
		return HttpResponse(request)

	args = {}
	args['user'    ] = request.user
	args['project' ] = Project.objects.get(id = id_project)
	args['tasks'   ] = Task.objects.filter(project = id_project)	

	try:
		args['iterations'] = Iteration.objects.filter(project = id_project)
	except Iteration.DoesNotExist:
		args['iterations'] = []

	return render_to_response('tasks.html', args)

def show_dashboard(request, id_project = 0, id_iteration = 0, id_user = 0):
	args = {}
	args.update(csrf(request))
	args['user'	   ] = request.user
	
	if id_project:
		args['project'] = Project.objects.get(id = id_project)
		try:
			args['iterations'] = Iteration.objects.filter(project = id_project).order_by('dead_line')
		except Iteration.DoesNotExist:
			args['iterations'] = []

	return render_to_response('dashboard.html', args)

def edit_task(request, id_task = '0'):
	if request.method == "POST":
		if id_task != '0':
			task = Task.objects.get(id = id_task) 
			form = TaskForm(request.POST, instance = task)
		else:
			form = TaskForm(request.POST,  request.FILES)

		if not form.is_valid():
			return HttpResponse("Форма не валидна")
		
		form.save()	

		return redirect(request.META.get('HTTP_REFERER','/'))
	else: # GET
		args={}	
		args.update(csrf(request))
		if 'id_task' in request.GET:
			id_task = int(request.GET['id_task'])
		if id_task != 0:
			task = Task.objects.get(id = id_task)
			args['form'] = TaskForm(instance = task)
		else:
			args['form'] = TaskForm()

		args['id_task'] = id_task
		return render_to_response('task.html', args)

def get_tasks(request, id_project = 0, id_iteration = 0, which_tasks = '0'):
	if request.method == 'POST':
		return HttpResponse("Ожидался метод GET")
		
	id_project 	    = request.GET['id_project']
	id_iteration 	= request.GET['id_iteration']
	which_tasks 	= request.GET['which_tasks']
	name_user 		= request.user
    
	if id_project :
		tasks = Task.objects.filter(project = id_project)
	else:
		tasks = Task.objects.filter()
	
	if id_iteration :
		tasks = tasks.filter(iterate = id_iteration)
			
	if which_tasks != '0' :
		tasks = tasks.filter(assigned = request.user.id)

	tasks = tasks.values('id', 'title', 'text', 'priority', 'assigned', 'type_task', 'status', 'iterate')

	tasks_to_do 		= []
	tasks_in_progress 	= []
	tasks_test			= []
	tasks_done			= []
	tasks_not_dev		= []
		
	for task in tasks:
		task['style'] = _get_style_priority(task['priority'])
		if task['status']   == "not_dev":
			tasks_not_dev.append(task)
		elif task['status'] ==	"to_do":	
			tasks_to_do.append(task)
		elif task['status'] == "in_progress":
			tasks_in_progress.append(task)
		elif task['status'] == "test":
			tasks_test.append(task)
		elif task['status'] == "done":
			tasks_done.append(task)

	data = json.dumps({'tasks_not_dev' : tasks_not_dev, 'tasks_in_progress' : tasks_in_progress, 'tasks_test' : tasks_test,  'tasks_done' : tasks_done,  'tasks_to_do' : tasks_to_do})

	return HttpResponse(data, mimetype='application/json') 

def _get_style_priority(priority):
	if priority == 0:
		return ""
	if priority > 4:
		return "priority_max"
	else:
		return "priority_" + str(priority)

def change_status(request, id_task = "", new_status = ""):
	id_task 	= request.GET['id_task']
	new_status  = request.GET['new_status']
	Task.objects.filter(id=id_task).update(status=new_status)

	return HttpResponse(request)
