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

	instruction = models.TextField(
		verbose_name = 'instruction',
		blank = True)

	prerequisite = models.ForeignKey(
		Quiz,
		verbose_name = 'prerequisite',
		blank = True)

	label_list = models.ManyToManyField(
		Label,
		blank = False,
		verbose_name = 'label list')

	post_list = models.ManyToManyField(
		Post,
		default = None,
		blank = True,
		verbose_name = 'post list')

	creator = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		verbose_name = 'creator',
		blank = False,
		null = False)

	def __unicode__(self):
		return self.title

