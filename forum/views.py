#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.core.context_processors import csrf
from project.models import Project
from comment.models import Comment
from forum.models import Forum
from forms import ForumForm
import logging
from django.core.cache import cache

def forum (request, id_project = 0):
	args = {}
	args['cache']  = cache.get_many( [ 'project_id', 'project_title', 'user_name' ] )
	args['forums'] = Forum.objects.filter(project = args['cache']['project_id'])
	return render_to_response('forum.html', args)

def edit_forum(request, id_forum = 0):
	if request.method == "POST":
		if id_forum:
			forum = Forum.objects.get(id = id_forum) 
			form  = ForumForm(request.POST, instance = forum)
		else:
			form = ForumForm(request.POST, request.FILES)

		if not form.is_valid():
			return HttpResponse("Форма не валидна")
		
		form.save()	

		return redirect(request.META.get('HTTP_REFERER','/'))
	else: # GET
		args={}	
		args.update(csrf(request))
		if 'id_forum' in request.GET:
			id_forum = int(request.GET['id_forum'])
		if id_forum != 0:
			task = Forum.objects.get(id = id_forum)
			args['form'] = ForumForm(instance = forum)
		else:
			args['form'] = ForumForm()

		return render_to_response('edit_forum.html', args)
