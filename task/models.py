#-*-coding: utf-8 -*-
from django.db import models
from iteration.models import Iteration
from django.contrib.auth.models import User
from project.models import Project
import datetime

class Task(models.Model):
	title = models.CharField(max_length = 200, verbose_name = "Название")
	text = models.TextField(verbose_name = "Описание", blank = False)	
	dead_line = models.DateTimeField(blank = True, default=datetime.datetime.now, verbose_name = "Последний срок")
	start_time = models.DateTimeField(blank = True, default=datetime.datetime.now)
	end_time = models.DateTimeField(blank = True, default=datetime.datetime.now)
	priority = models.IntegerField(default = 0, verbose_name = "Приоритет")
	updated = models.DateTimeField(blank = True, default=datetime.datetime.now)
	
	iterate = models.ForeignKey(Iteration, verbose_name = "Итерация", blank = True, null = True)
	assigned = models.ForeignKey(User, verbose_name = "Исполнитель", related_name='assigned', blank = True, null = True)
	entrasted = models.ForeignKey(User, verbose_name = "Назначил", related_name='entrasted', blank = True, null = True)
	main_task = models.ForeignKey('self', verbose_name = "Главная задача", blank = True, null = True)
	project = models.ForeignKey(Project, verbose_name = "Проект", blank = True, null = True)

	TYPES_TASKS = (
	    ('bug', 'Bug'),
	    ('improve', 'Improve'),
	    ('task', 'Task'),
	)

	STATUS_TASKS = (
		('not_dev', 'Not dev'),
	    ('to_do', 'To do'),
	    ('in_progress', 'In progress'),
	    ('test', 'Test'),
	    ('done', 'Done'),
	)
	type_task = models.CharField(max_length = 7, choices = TYPES_TASKS, default = 'task', verbose_name = "Тип задачи")
	status = models.CharField(max_length = 11, choices = STATUS_TASKS, default = 'not_dev')

	def __unicode__(self):
		return self.title