#-*-coding: utf-8 -*-
from django.http.response 			import HttpResponse, Http404
from django.shortcuts 				import render_to_response, redirect
from django.core.exceptions 		import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.paginator 			import Paginator
from django.shortcuts 				import HttpResponseRedirect

from django.contrib            import auth
from auth.forms                import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.core.cache import cache
import logging

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



