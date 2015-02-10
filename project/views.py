#-*-coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from project.models import Project
from forms import ProjectForm
from django.contrib.auth.models import User

# Create your views here.
def create(request):
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponse("Вы создали и сохранили новую форму проекта")
	else:
		form = ProjectForm()
		args = {}
		args.update(csrf(request))
		args['form'] = form
		return HttpResponse("Вы не создали новую форму проекта. И остались на странице создания")

def new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			#leader = User.objects.get(username = request.POST['name_leader'])
			#request.POST['leader_id'] = leader.id
			form.save()
			return redirect('/projects')
		return HttpResponse("Форма не валидна")

	#users = User.objects.all()
	user = request.user

	args = {}
	#args['users'] = users
	args.update(csrf(request))
	args['user'] = user
	args['form'] = ProjectForm()
	args['projects'] = Project.objects.all()	
	return render_to_response('new.html', args)

def projects(request):
	user = request.user
	
	args = {}
	args['user'] = user
	args['projects'] = Project.objects.all() 

	return render_to_response('projects.html', args)

def show_project(request, id_project = 0):
	user = request.user

	args = {}
	args['user'] = user
	args['projects'] = Project.objects.all() 
	args['project'] = Project.objects.get(id = id_project)
	return render_to_response('project.html', args)
