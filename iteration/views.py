#-*-coding: utf-8 -*-
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from django.shortcuts     import render_to_response, redirect
from django.core.cache    import cache
from project.models       import Project
from forms                import IterationForm
from models               import Iteration
from datetime             import datetime, timedelta
import json
import logging

def iterates(request):
	args = {}
	args['cache']        = cache.get_many( ['project_id', 'project_title', 'user_name'] )
	args['iterates']     = Iteration.objects.filter(project = args['cache']['project_id']).values('id', 'title', 'start_line', 'dead_line', 'project')	
	args['iterate_days'] = Project.objects.filter(id = args['cache']['project_id']).values('iterate_days')[0]['iterate_days']
	if not args['iterate_days']:
		args['iterate_days'] = "не указано"
	return render_to_response('iterates.html', args)

def iterate(request, iterate_id = 0 ):
	if request.method == "POST":
		if iterate_id != 0:
			iterate = Iteration.objects.get(id = iterate_id) 
			form = IterationForm(request.POST, instance = iterate)
		else:
			form = IterationForm(request.POST,  request.FILES)

		if not form.is_valid():
			return HttpResponse("Форма не валидна")
		
		form.save()	

		return redirect(request.META.get('HTTP_REFERER','/'))
	else: # GET
		args={}	
		args.update(csrf(request))
		if iterate_id != 0:
			iterate = Iteration.objects.get(id = iterate_id)
			args['form'] = IterationForm(instance = iterate)
			args['iterate_id'] = iterate.id
		else:
			args['form'] = IterationForm()

		return render_to_response('iterate.html', args)

def set_iterate_days(request):
	if 'new_count_days' in request.GET:
		new_count_days = request.GET['new_count_days']
		Project.objects.filter(id = cache.get('project_id')).update(iterate_days = new_count_days)	
		return HttpResponse()
	else:
		return Http404
	
	
	
	