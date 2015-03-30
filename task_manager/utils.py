#-*-coding: utf-8 -*-
from iteration.models  import Iteration
from project.models    import Project
from task.models       import Task
from django.core.cache import cache
from datetime          import datetime, timedelta

def get_current_iterate(project_id = 0):
	today_time  = datetime.now
	cur_iterates = Iteration.objects.filter(project_id = project_id, dead_line__gt = today_time, start_line__lt = today_time )
	if cur_iterates:
		return cur_iterates[0].id
	else:
		pre_iterates = Iteration.objects.filter(project_id = project_id, start_line__lt = today_time ).order_by('-start_line')
		if pre_iterates:
			tasks = Task.objects.filter(iterate = pre_iterates[0].id).exclude(status = "done")

		next_iterates = Iteration.objects.filter(project_id = project_id, start_line__gt = today_time ).order_by('start_line')
		if not next_iterates:
			cur_project    = Project.objects.filter(id = project_id).values('iterate_days')[0]
			iterate_days_t = timedelta( days = cur_project['iterate_days'] )
			start_line     = datetime.now()
			dead_line      = start_line + iterate_days_t
			next_iterate   = Iteration.objects.create(title = "default title", project_id = project_id, start_line = start_line, dead_line = dead_line)
			next_iterate.save()
		else:
			next_iterate = next_iterates[0].id

		if tasks:
			tasks.update( iterate = next_iterate )

	return next_iterate.id

def get_users_project(project_id):
	project_id = project_id if project_id else cache.get('project_id')
	dict_users = Task.objects.filter(project = project_id).exclude(assigned = None).values('assigned', 'assigned__username').distinct()
	lst_id = [ user['assigned'] for user in dict_users ]
	return { 
		'dict_users' : dict_users,
		'lst_id'     : lst_id
	}