#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from task.models import Task
from project.models import Project
from forms import TaskForm
from iteration.models import Iteration
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import json
import logging
from datetime import datetime, timedelta
from django.utils import timezone

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

def task(request, id_task = '0', contents = 'describe'):
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
		contents = request.GET['contents']
		if 'id_task' in request.GET:
			id_task = int(request.GET['id_task'])
		if id_task != 0:			
			if contents == 'describe':
				args['task'] = Task.objects.filter(id = id_task).values('title', 'id', 'text', 'project__title', 'iterate__title', 'type_task', 'status', 'assigned__username', 'entrasted__username')[0]
			else:
				task = Task.objects.get(id = id_task)
				args['form'] = TaskForm(instance = task)
				args['task_id'] = task.id
		else:
			args['form'] = TaskForm()

		tmpl = contents + '_task.html'
		return render_to_response(tmpl, args)

def show_task(request, id_task = '0'):
	args = {}
	if 'id_task' in request.GET:
		id_task = int(request.GET['id_task'])
	if id_task != 0:
		args['task'] = Task.objects.filter(id = id_task).values('title', 'id', 'text', 'project__title', 'iterate__title', 'type_task', 'status', 'assigned__username', 'entrasted__username')[0]

	return render_to_response('task.html', args)

def get_tasks(request, id_project = 0, id_iteration = 0, which_tasks = '0'):
	if request.method == 'POST':
		return HttpResponse("Ожидался метод GET")
		
	id_project 	    = request.GET['id_project']   if ('id_project' in request.GET) else 0
	id_iteration 	= request.GET['id_iteration'] if ('id_iteration' in request.GET) else 0
	which_tasks 	= request.GET['which_tasks']  if ('which_tasks' in request.GET) else 0
	name_user 		= request.user
    
	if id_project :
		try:
			tasks = Task.objects.filter(project = id_project)
		except Task.ObjectDoesNotExist:
			return HttpResponse( json.dumps( { 'empty' : 1 } ), mimetype='application/json')
	else:
		try:
			tasks = Task.objects.filter()
		except Task.ObjectDoesNotExist:
			return HttpResponse( json.dumps( { 'empty' : 1 } ), mimetype='application/json')

	if tasks == []:
		return HttpResponse( json.dumps( { 'empty' : 1 } ), mimetype='application/json')
	
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

def get_progress_bar_user(request, id_iterate = '0', id_user = '0'):
	if id_user == '0':
		id_user = request.session['_auth_user_id']
	else:
		id_user = int(id_user)

	if id_iterate != '0':
		iterate = Iteration.objects.filter(id = id_iterate).values('start_line', 'dead_line')[0]
		iterate_time = { 
			'start_line' : iterate['start_line'].strftime('%Y-%m-%d %H:%M'),
			'dead_line'  : iterate['dead_line' ].strftime('%Y-%m-%d %H:%M'),
		}
	else:
		iterate_time = { 'start_line' : 'Нет текущей итерации'}
	
	tasks  = Task.objects.filter( Q(assigned = id_user) & Q(iterate = id_iterate) & ( Q(status = 'in_progress') | Q(status = 'done') ) ).order_by('-status').values('status', 'start_time', 'end_time', 'title', 'id', 'priority')
	to_progress_bar = []
	sum_work_time = timedelta(0)
	today_time = timezone.now()

	for task in tasks:
		if task['status'] == "done":
			task['perform_time'] = task['end_time'] - task['start_time']
		else:
			task['perform_time'] = today_time - task['start_time']
		sum_work_time += task['perform_time']

	for task in tasks:
		data_task = { 
			'id'           : task['id'],
			'width'        : (task['perform_time'].total_seconds() * 100) / sum_work_time.total_seconds(),
			'perform_time' : str(task['perform_time']).split('.')[0],
			'title'        : task['title'],
			'css_class'    : 'progress-bar-striped active '+_get_class_progress_by_priority(task['priority']) if task['status'] == 'in_progress' else _get_class_progress_by_priority(task['priority'])
		}
		to_progress_bar.append(data_task)
	return HttpResponse(json.dumps({ 'all_time': str(sum_work_time).split('.')[0], 'progress_bar' : to_progress_bar, 'iterate_time' : iterate_time }), content_type='application/json')

def _get_class_progress_by_priority(priority):
	if priority == 0:
		return ''
	elif priority == 1:
		return 'progress-bar-warning'
	elif priority == 2:
		return 'progress-bar-success'
	elif priority == 3:
		return 'progress-bar-info'
	elif priority == 4:
		return 'progress-bar-danger'
	else:
		return 'progress-bar-black'


def change_status(request, id_task = "", new_status = ""):
	args = {}
	id_task    = request.GET['id_task']
	task = Task.objects.get(id = id_task)	
	new_status = request.GET['new_status']
	
	if task.status == "to_do" and new_status == "in_progress":
		start_time = datetime.now()	
		Task.objects.filter(id = id_task).update(status = new_status, start_time = start_time)	
	elif new_status == "done":
		end_time = datetime.now()
		Task.objects.filter(id = id_task).update(status = new_status, end_time = end_time)
	else:
		Task.objects.filter(id = id_task).update(status = new_status)
	
	return HttpResponse(request)
