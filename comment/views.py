from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from models import Comment
from forum.models import Forum
import datetime
import logging


def create(request, id_forum = 0):
	if request.method == "GET":
		user = request.user
		if 'id_forum' in request.GET:
			id_forum = int(request.GET['id_forum'])
		if 'text' in request.GET:
			text = request.GET['text']
			
		forum = Forum.objects.get(id = id_forum)
		form = Comment( text = text, forum = forum, user = user)
		form.save()
		args = {}
		args['comment'] = {
			'text'     : text,
			'updated'  : datetime.datetime.now,
			'username' : user.username,
		}
		return render_to_response('comment.html', args)
	return HttpResponse("Expected method GET - get GET")
