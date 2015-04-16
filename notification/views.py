#-*-coding: utf-8 -*-
from django.shortcuts    import render, render_to_response, redirect
from django.core.cache   import cache
from notification.models import Notification

def get_notification(request):
	user_id = cache.get('user_id')	
	action = request.GET['action'] if ('action' in request.GET) else 'assigned'

	if action == "added":
		text = "Появились новые задачи, которым нужен исполнитель:"
		notifications = Notification.objects.filter(action=action, project=cache.get('project_id')).values('task__title', 'task__id', 'created', 'readed')
	else:
		notifications = Notification.objects.filter(user=user_id, action=action).values('task__title', 'task__id', 'created', 'readed')
		if action == "assigned":
			text = "Вас назначили исполнителем следующих задач:"
		else:
			text = "Произошла смена итерации. Все не выполненные вами задачи в предыдущей итерации перешли на новою:"
	readed_notes = []
	new_notes =[]
	for note in notifications:
		if note['readed']:
			readed_notes.append(note)
		else:
			new_notes.append(note)
	
	notifications.update(readed=True)

	return render_to_response('notification.html', {'readed_notes' : readed_notes, 'new_notes' : new_notes, 'text': text})
