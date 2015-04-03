#-*-coding: utf-8 -*-
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts       import render_to_response, redirect
from task_manager.utils     import get_users_project
from django.http.response   import HttpResponse, Http404
from task.models            import Task
from project.models         import Project
from iteration.models       import Iteration
from django.db.models       import Q
from datetime               import datetime, timedelta
from django.utils           import timezone
from django.core.cache      import cache
from django.db.models       import Count
import json
import logging

def statistic_users(request):
	args = {}
	args['cache'] = cache.get_many( [ 'project_id', 'user_name', 'project_title', 'iterate_id' ])
	users         = get_users_project( args['cache']['project_id'] )['dict_users']
	iterate_id    = request.GET['iterate_id'] if 'iterate_id' in request.GET else cache.get('iterate_id')
	data_users = []
	for user in users:
		data_users.append({
			'user_name' : user['assigned__username'],
			'user_id'   : user['assigned'],
		})

	args['data_users'] = data_users

	try:
		args['iterations'] = Iteration.objects.filter(project = args['cache']['project_id'] ).values('title', 'id')
	except Iteration.DoesNotExist:
		args['iterations'] = []

	return render_to_response('statistic.html', args)

def get_progress_bar_user(request, user_id = None, iterate_id = None):
	for_statistic = False
	if 'user_id' in request.GET:
		user_id = request.GET['user_id']
	elif not user_id:
		user_id = cache.get('user_id')
	else:
		for_statistic = True

	if 'iterate_id' in request.GET:
		iterate_id = request.GET['iterate_id']
	elif not iterate_id:
		iterate_id = cache.get('iterate_id')	
	
	tasks  = Task.objects.filter( Q(assigned = user_id) & Q(iterate = iterate_id) & ( Q(status = 'in_progress') | Q(status = 'done') ) ).order_by('-status').values('status', 'start_time', 'end_time', 'title', 'id', 'priority')
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

	res_data = { 'all_time': str(sum_work_time).split('.')[0], 'progress_bar' : to_progress_bar}
	if not for_statistic:
		return HttpResponse(json.dumps(res_data), content_type='application/json')
	else:
		return res_data

def get_progress_users(request, iterate_id = None, lst_users_id = []):
	iterate_id   = request.GET['iterate_id'] if 'iterate_id' in request.GET else cache.get('iterate_id')
	lst_users_id = json.loads(request.GET['lst_users_id']) if 'lst_users_id' in request.GET else []

	data_users = {}
	for user_id in lst_users_id:
		data_users[user_id] = get_progress_bar_user( request = request, user_id = user_id, iterate_id = iterate_id )	

	iterate = Iteration.objects.filter(id = iterate_id).values('start_line', 'dead_line')[0]
	iterate_time = { 
		'start_line' : iterate['start_line'].strftime('%Y-%m-%d %H:%M'),
		'dead_line'  : iterate['dead_line' ].strftime('%Y-%m-%d %H:%M'),
	}

	args = {}
	args['data_users']   = data_users	
	args['iterate_time'] = iterate_time

	return HttpResponse(json.dumps(args), content_type='application/json')

def get_data_graphic(request, iterate_id = None):
	iterate_id = request.GET['iterate_id'] if 'iterate_id' in request.GET else cache.get('iterate_id')
	tasks      = Task.objects.filter( iterate = iterate_id, status = "done" ).values( 'id', 'title', 'start_time', 'end_time' )

	iterate = Iteration.objects.filter(id = iterate_id).values('start_line', 'dead_line')[0]
	iterate_time = { 
		'start_line' : iterate['start_line'],
		'dead_line'  : iterate['dead_line' ],
	}

	data_tasks = []
	starting_point = iterate_time['start_line']
	for task in tasks:
		perform_time = task['end_time'] - task['start_time']
		data_tasks.append(
			{
				'id_task'      : task['id'],
				'title_task'   : task['title'],
				'x_coordinate' : starting_point.strftime('%Y-%m-%d %H:%M'),
				'perform_time' : str(perform_time),
			}
		)
		starting_point = starting_point + perform_time	

	iterate = Iteration.objects.filter(id = iterate_id).values('start_line', 'dead_line')[0]
	iterate_time = { 
		'start_line' : iterate['start_line'].strftime('%Y-%m-%d %H:%M'),
		'dead_line'  : iterate['dead_line' ].strftime('%Y-%m-%d %H:%M'),
	}

	args = {}
	args['data_tasks']   = data_tasks	
	args['iterate_time'] = iterate_time
	args['count_tasks']  = Task.objects.filter(iterate = iterate_id).count()

	return HttpResponse(json.dumps(args), content_type='application/json')


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
