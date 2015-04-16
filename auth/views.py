#-*-coding: utf-8 -*-
from django.http.response 			import HttpResponse, Http404
from django.shortcuts 				import render_to_response, redirect
from django.core.exceptions 		import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.shortcuts 				import HttpResponseRedirect

from django.contrib            import auth
from auth.forms                import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
from project.models    import Project
from task.models       import Task
from notification.models import Notification
from user_profile.models import UserProfile
from task_manager.utils import get_projects_user, get_current_iterate
from datetime import datetime, timedelta
import logging

def set_data_after_logging(request):
	user = request.user
	user_id = user.id
	cache.delete_many( [ 'project_id', 'iterate_id' ])
	cache.set_many( { 'user_id' : user_id, 'user_name' : user.username })
	UserProfile.objects.filter(user_id = user_id).update(last_visit = datetime.now())
	Notification.objects.filter(created__lte = datetime.now() - timedelta(days=10)).delete()
	
	projects  = get_projects_user(user_id)
	if projects:
		project_id = projects[0]['id']			
		iterate_id = get_current_iterate(project_id)
		cache.set_many( { 
				'project_id'   : project_id,
				'project_title': projects[0]['title'],
				'iterate_id'   : iterate_id
			} )

	return redirect('/auth')

def auth_form(request):
	if request.user.id :
		return redirect('/projects')
	args = {'error' : 'hide'}
	args.update(csrf(request))
	args['form'] = AuthenticationForm

	return render_to_response('auth.html', args)

def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user = auth.authenticate(username=request.POST['username'], password=request.POST['password1'])
			auth.login(request, user)
			return redirect('/auth')
		return('форма не валидна')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')



