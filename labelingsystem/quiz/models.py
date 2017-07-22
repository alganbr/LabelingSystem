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
class Quiz(models.Model):
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
        related_name="quiz_category")

    max_questions = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="max_questions",
        help_text="Number of questions to be answered")

    pass_mark = models.SmallIntegerField(
        blank=True,
        default=0,
        verbose_name="pass_mark",
        help_text="Percentage required to pass",
        validators=[MaxValueValidator(100)])

    random_order = models.BooleanField(
        blank=False, default=False,
        verbose_name="random_order",
        help_text="Display the questions in a random order or as they are set")

    single_attempt = models.BooleanField(
        blank=False, default=False,
        verbose_name="single_attempt",
        help_text="If yes, only one attempt by a user will be permitted")

    question_list = models.ManyToManyField(
        Question,
        default=None,
        blank=True,
        verbose_name="question_list",
        help_text="The questions in the quiz")

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="creator",
        blank=False,
        null=False,
        help_text="The creator of the quiz")

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.pass_mark > 100:
            raise ValidationError('%s is above 100' % self.pass_mark)

        super(Quiz, self).save(force_insert, force_update, *args, **kwargs)

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name="quiz"
        verbose_name_plural="quizzes"

    def __unicode__(self):
        return self.title
