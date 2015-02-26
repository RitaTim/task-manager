#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http.response import HttpResponse, Http404
from project.models import Project
from comment.models import Comment
from forum.models import Forum
import logging

def forum (request):
	args = {}
	args['user']     = request.user
	args['projects'] = Project.objects.all() 
	args['forums']   = Forum.objects.all()

	return render_to_response('forum.html', args)

def get_comments (request, id_forum = 0):
	args = {}
	if 'id_forum' in request.GET:
		id_forum = request.GET['id_forum']
	args['comments'] = Comment.objects.filter(forum = request.GET['id_forum']).values('text', 'updated', 'user__username')
	args['forum']    = Forum.objects.get(id = id_forum)
	return render_to_response('comments.html', args)
