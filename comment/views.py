#-*-coding: utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from models import Comment
from forum.models import Forum
from task.models import Task
import datetime
import logging


def create(request, id_forum = 0, id_task = 0):
	if request.method == "GET":
		user = request.user
		if 'text' in request.GET:
			text = request.GET['text']

		if 'id_forum' in request.GET:
			id_forum = int(request.GET['id_forum'])
			forum = Forum.objects.get(id = id_forum)
			form = Comment( text = text, forum = forum, user = user)
			form.save()
		if 'id_task' in request.GET:
			id_task = int(request.GET['id_task'])
			task = Task.objects.get(id = id_task)
			form = Comment( text = text, task = task, user = user)
			form.save()
		
		args = {}
		args['comment'] = {
			'text'     : text,
			'updated'  : datetime.datetime.now,
			'username' : user.username,
		}
		return render_to_response('comment.html', args)
	return HttpResponse("Expected method GET - get GET")

def get_comments (request, id_forum = 0, id_task = 0):
	args = {}
	if 'id_forum' in request.GET:
		id_forum = int(request.GET['id_forum'])
		args['comments'] = Comment.objects.filter(forum = request.GET['id_forum']).values('text', 'updated', 'user__username')
		args['forum']    = Forum.objects.get(id = id_forum)
		args['title']    = args['forum'].title
	if 'id_task' in request.GET:
		id_task = int(request.GET['id_task'])
		args['comments'] = Comment.objects.filter(task = request.GET['id_task']).values('text', 'updated', 'user__username')
		args['task']     = Task.objects.get(id = id_task)
		args['title']    = "Комментарии"
	return render_to_response('comments.html', args)