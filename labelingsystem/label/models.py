from django.db import models
from post.models import Post

# Create your models here.
class Label(models.Model):

	class Meta:
		verbose_name = 'label'
		verbose_name_plural = 'labels'

	content = models.CharField(
		max_length = 1000,
		blank = False,
		verbose_name = 'content')

	def __unicode__(self):
		return self.content