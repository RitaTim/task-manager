# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    avatar = models.ImageField(verbose_name='Аватар', upload_to='images/%Y/%m/%d', blank=True, null=True)
    date_of_birth = models.DateField(verbose_name='День рождения', blank=True, null=True)
    level = models.IntegerField(verbose_name='Уровень', default = 0)


def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user = u)[0])