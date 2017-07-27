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
		return "user: " + str(self.user.username) + "; quiz: " + str(self.quiz.title)

class TaskResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	task = models.ForeignKey(Task)
	score = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "user: " + str(self.user.username) + "; quiz: " + str(self.task.title)

class QuestionResponse(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)
	correct = models.BooleanField(default=False)
	quiz_response = models.ManyToManyField(QuizResponse, blank=True)
	task_response = models.ManyToManyField(TaskResponse, blank=True)

	def __unicode__(self):
		return "user: " + str(self.user.username) + "; question: " + str(self.question.content)