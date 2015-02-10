#-*-coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect
#from django.contrib.formtools.wizard.views import SessionWizardView
#from django.core.mail import send_mail
#import logging
#logr = logging.getLogger(__name__)

#from article.forms import CommentForm
#from article.models import Article, Comments
from django.contrib import auth
from django.contrib.auth import *
from auth.forms import MyRegistrationForm

from auth.forms import UserCreationForm

# Create your views here.
def auth(request):
	c = {'error' : 'hide'}
	c.update(csrf(request))
	return render_to_response('auth.html', c)


def login_user(request):
	args = {}
	args.update(csrf(request))
	
	username = request.POST.get['username', '']
	password = request.POST.get['password', '']
	user = auth.authenticate(username = username, password = password)

	if user is not None:
		if user.is_active:
			auth.login(request, user)
			return redirect("/projects")#render_to_response('logged_in.html', {'last_name' : request.user.username}) #redirect('/auth/logged_in')
		else: 
			return HttpResponse("User not active")
	else:
		return render_to_response('auth.html', {'error' : 'show'})


def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/auth')

#def logged_in(request):
	#c = {}
	#c.update(csrf(request))
	#return render_to_response('logged_in.html', {'last_name' : request.user.username})

def register(request):
	if request.method == "POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/auth/register_success')
		return('форма не валидна')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')



