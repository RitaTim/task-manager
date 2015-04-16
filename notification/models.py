#-*-coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from task.models  import Task
from project.models  import Project

import datetime

class Notification(models.Model):
	ACTIONS = (
	    ('added', 'Added'),
	    ('assigned', 'Assigned'),
	    ('changed_iter', 'Change iteration'),
	)

	action = models.CharField(max_length=12, choices=ACTIONS, default='added', verbose_name="Тип оповещения")
	user = models.ForeignKey(User, verbose_name="Пользователь", blank=True, null=True)
	project = models.ForeignKey(Project, verbose_name="Проект", blank=True, null=True)
	task = models.ForeignKey(Task,  verbose_name="Задача", blank=True, null=True)
	readed = models.BooleanField(default=False)
	created = models.DateTimeField(default=datetime.datetime.now)


	
