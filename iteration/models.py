#-*-coding: utf-8 -*-
from django.db import models
from project.models import Project

# Create your models here.
class Iteration(models.Model):
	title      = models.CharField(max_length = 200)
	dead_line  = models.DateTimeField(blank = True)
	start_line = models.DateTimeField(blank = True)

	project = models.ForeignKey(Project, verbose_name = "Проект", default=lambda: Project.objects.get(id=1))
	
	def __unicode__(self):
		return self.title