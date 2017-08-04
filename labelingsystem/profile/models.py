# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from quiz.models import Quiz
from task.models import Task
from response.models import QuizResponse, TaskResponse

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE)

	profile_pic = models.ImageField(
		blank = True,
		upload_to = 'profile_pics')

	training_mode = models.BooleanField(
		default = 1)

	quiz_list = models.ManyToManyField(
		Quiz,
		verbose_name = "quiz_list",
		related_name = "quiz_list",
		blank = True)

	task_list = models.ManyToManyField(
		Task,
		verbose_name = "task_list",
		related_name = "task_list",
		blank = True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
