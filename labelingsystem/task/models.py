from django.db import models
from django.conf import settings

from label.models import Label
from post.models import Post
from quiz.models import Quiz

# Create your models here.
class Task(models.Model):

	class Meta:
		verbose_name = 'task'
		verbose_name_plural = 'tasks'

	title = models.CharField(
		max_length = 50,
		verbose_name = 'title',
		blank = False)

	description = models.TextField(
		verbose_name = 'description',
		blank = True)

	prerequisite = models.ForeignKey(
		Quiz,
		verbose_name = 'prerequisite',
		blank = True,
		null = True)

	label_list = models.ManyToManyField(
		Label,
		blank = True,
		default = None,
		verbose_name = 'label list')

	post_list = models.ManyToManyField(
		Post,
		blank = True,
		default = None,
		verbose_name = 'post list')

	creator = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		verbose_name = 'creator',
		blank = False,
		default = None,
		null = False)

	def __str__(self):
		return self.title

class Participation(models.Model):

	class Meta:
		verbose_name = 'participation'
		verbose_name_plural = 'participantions'
		unique_together = ('task', 'coder')

	task = models.ForeignKey(
		Task,
		on_delete = models.CASCADE,
		blank = False,
		default = None,
		verbose_name = 'task')

	coder = models.EmailField(
		blank = False,
		default = None,
		verbose_name = 'coder')

	def __str__(self):
		return '{0} | {1}'.format(self.task, self.coder)


