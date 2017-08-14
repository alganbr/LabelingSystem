from django.db import models
from django.core.validators import MaxValueValidator

from django.conf import settings
from label.models import Label
from post.models import Post

# Create your models here.
class Quiz(models.Model):
	
	class Meta:
		verbose_name = 'quiz'
		verbose_name_plural = 'quizzes'

	title = models.CharField(
		max_length = 50,
		verbose_name = 'title',
		blank = False)

	instruction = models.TextField(
		verbose_name = 'instruction',
		blank = True)

	max_posts = models.PositiveIntegerField(
		blank = True,
		null = True,
		verbose_name = 'max posts')

	pass_mark = models.PositiveIntegerField(
		blank = True,
		default = 0,
		verbose_name = 'pass mark',
		validators = [MaxValueValidator(100)])

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

class AnswerKey(models.Model):

	class Meta:
		verbose_name = 'answer key'
		verbose_name_plural = 'answer keys'

	quiz = models.ForeignKey(
		Quiz,
		blank = False)

	def __unicode__(self):
		return "{} answer key".format(self.quiz)

class Answer(models.Model):

	class Meta:
		verbose_name = 'answer'
		verbose_name_plural = 'answers'

	answer_key = models.ForeignKey(
		AnswerKey,
		blank = False)

	post = models.ForeignKey(
		Post,
		blank = False)

	label = models.ForeignKey(
		Label,
		blank = False)

	def __unicode__(self):
		return self.post + " -> " + self.label

class QuizResponse(models.Model):

	class Meta:
		verbose_name = 'quiz response'
		verbose_name_plural = 'quiz responses'

	responder = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		blank = False,
		verbose_name = 'responder')

	quiz = models.ForeignKey(
		Quiz,
		on_delete = models.CASCADE,
		blank = False,
		verbose_name = 'quiz')

	score = models.PositiveIntegerField(
		default = 0,
		validators = [MaxValueValidator(100)])

	timestamp = models.DateTimeField(
		auto_now_add = True)



