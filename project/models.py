#-*-coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

def get_uploaded_file_name(instance, filename):
	return "images/%s" % filename

class Project(models.Model):
	title 		 = models.CharField(max_length=200, verbose_name="Название проекта")
	text 		 = models.TextField(verbose_name="Описание проекта")
	leader  	 = models.ForeignKey(User, verbose_name="Руководитель проекта", default=lambda: User.objects.get(id=1))
	logo 		 = models.ImageField(upload_to=get_uploaded_file_name, verbose_name="Логотип проекта", blank=True)
	create_date  = models.DateField(blank=True, null=True, verbose_name="Дата создания")
	iterate_days = models.IntegerField(default=14, verbose_name="Количество дней в итерации")

	def __unicode__(self):
		return self.title