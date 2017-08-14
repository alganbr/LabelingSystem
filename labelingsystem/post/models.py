from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):

	class Meta:
		verbose_name = 'post'
		verbose_name_plural = 'posts'

	content = models.CharField(
		max_length = 1000,
		blank = False,
		verbose_name = 'post')

	author = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		verbose_name = 'creator',
		blank = False,
		null = False)

	def __unicode__(self):
		return self.content

class PostResponse(models.Model):

	class Meta:
		verbose_name = 'post response'
		verbose_name_plural = 'post responses'

	responder = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete = models.CASCADE,
		blank = False,
		verbose_name = 'responder')

	post = models.ForeignKey(
		Post,
		on_delete = models.CASCADE,
		blank = False,
		verbose_name = 'post')

	timestamp = models.DateTimeField(
		auto_now_add = True)


