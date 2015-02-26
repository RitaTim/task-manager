# -*- coding: utf-8 -*-
from django.db 	  import models
from forum.models import Forum
from task.models  import Task
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Comment(models.Model):
	text    = models.TextField(verbose_name = "Комментарий")
	
	updated = models.DateTimeField(blank = True, default=datetime.datetime.now)
	forum   = models.ForeignKey(Forum, verbose_name = "Форум",  blank = True, null = True)
	task    = models.ForeignKey(Task,  verbose_name = "Задача", blank = True, null = True)
	user    = models.ForeignKey(User,  verbose_name = "Автор",  blank = True)


	def __unicode__(self):
		return self.text