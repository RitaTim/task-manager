# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


def get_uploaded_file_name(instance, filename):
	return "images/%s" % filename

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    date_of_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)
    last_visit = models.DateField(verbose_name='День последнего посещения', blank=True, null=True)
    avatar = models.ImageField(verbose_name = 'Аватар', upload_to = get_uploaded_file_name, blank=True, null=True)
    level = models.IntegerField(verbose_name='Уровень', default = 0)
    phone = models.CharField(max_length = 20, default = '-', verbose_name = 'Контактный телефон',  blank=True, null=True)
    post = models.CharField(max_length = 20, default = '-', verbose_name = 'Должность',  blank=True, null=True)

def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])