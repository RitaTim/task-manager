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

def forum (request, id_project = 0):
	args = {}
	args['user']     = request.user
	args['project']  = Project.objects.get(id = id_project)
	args['forums']   = Forum.objects.filter(project = id_project)

	return render_to_response('forum.html', args)

def get_comments (request, id_forum = 0):
	args = {}
	if 'id_forum' in request.GET:
		id_forum = int(request.GET['id_forum'])
	args['comments'] = Comment.objects.filter(forum = request.GET['id_forum']).values('text', 'updated', 'user__username')
	args['forum']    = Forum.objects.get(id = id_forum)
	return render_to_response('comments.html', args)

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
