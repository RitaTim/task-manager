#-*-coding: utf-8 -*-
from django.db import models
from project.models import Project
from django.core.cache import cache

# Create your models here.
class Forum(models.Model):
	title = models.CharField(max_length = 200)	

	project = models.ForeignKey(Project, verbose_name = "Проект", default=lambda: Project.objects.get(id=cache.get('project_id')))


	def __unicode__(self):
		return self.title