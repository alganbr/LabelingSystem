# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from category.models import Category
from django.conf import settings

# Create your models here.
class Question(models.Model):
    
    category = models.ForeignKey(
    	Category,
        verbose_name="category",
        related_name="question_category",
        blank=True,
        null=True)

    content = models.CharField(
        max_length=1000,
        blank=False,
        verbose_name="question",
        help_text="Enter the question text")

    explanation = models.TextField(
        max_length=2000,
        blank=True,
        verbose_name="explanation",
        help_text="Explanation to be shown after the question has been answered")

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="creator",
        blank=False,
        null=False,
        help_text="The creator of the quiz")

    class Meta:
        verbose_name="question"
        verbose_name_plural="questions"
        ordering = ['category']

    def __unicode__(self):
        return self.content