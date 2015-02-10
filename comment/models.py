# -*- coding: utf-8 -*-
from django.db import models
from forum.models import Forum
from task.models import Task
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
	text = models.TextField()
	
	updated = models.DateTimeField(blank = True)
	forum = models.ForeignKey(Forum, verbose_name = "Форум", blank = True)
	task = models.ForeignKey(Task, verbose_name = "Задача", blank = True)
	user = models.ForeignKey(User, verbose_name = "Автор", blank = True)


	def __unicode__(self):
		return self.updated