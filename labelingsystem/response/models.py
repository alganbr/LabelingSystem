# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from question.models import Question
from quiz.models import Quiz
from task.models import Task

# Create your models here.
class QuizResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	quiz = models.ForeignKey(Quiz)
	score = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "Quiz response {0}".format(self.pk)

class TaskResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	task = models.ForeignKey(Task)
	score = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "Task response {0}".format(self.pk)

class QuizQuestionResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)
	quiz_response = models.ForeignKey(QuizResponse)

	def __unicode__(self):
		return "Quiz Question response {0}".format(self.pk)

class TaskQuestionResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)
	task_response = models.ForeignKey(TaskResponse)

	def __unicode__(self):
		return "Task Question response {0}".format(self.pk)