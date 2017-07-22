# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from question.models import Question

# Create your models here.
class Answer(models.Model):

    question = models.ForeignKey(
    	Question,
        verbose_name="question")

    content = models.CharField(
        max_length=1000,
        blank=False,
        verbose_name="content",
        help_text="Enter the answer text")

    correct = models.BooleanField(
        blank=False,
        default=False,
        verbose_name="correct",
        help_text="Is this a correct answer?")

    class Meta:
        verbose_name="answer"
        verbose_name_plural="answers"

    def __unicode__(self):
        return self.content