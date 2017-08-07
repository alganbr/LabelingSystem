# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.conf import settings

from category.models import Category
from question.models import Question

# Create your models here.
# Create your models here.
class Task(models.Model):
    title = models.CharField(
        verbose_name="title",
        max_length=60, 
        blank=False)

    description = models.TextField(
        verbose_name="description",
        blank=True,
        help_text="a description of the quiz")

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        verbose_name="category",
        related_name="task_category")

    question_list = models.ManyToManyField(
        Question,
        default=None,
        blank=True,
        verbose_name="question_list",
        help_text="The questions in the quiz")

    random_order = models.BooleanField(
        blank=False, default=False,
        verbose_name="random_order",
        help_text="Display the questions in a random order or as they are set")

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="creator",
        blank=False,
        null=False,
        help_text="The creator of the quiz")

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name="task"
        verbose_name_plural="tasks"

    def __unicode__(self):
        return self.title
