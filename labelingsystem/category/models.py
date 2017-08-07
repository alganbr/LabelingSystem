# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class CategoryManager(models.Manager):
    def new_category(self, category):
        new_category = self.create(category=re.sub('\s+', '-', category).lower())
        new_category.save()
        return new_category

class Category(models.Model):
    category = models.CharField(
        max_length=250,
        blank=True,
        null=True)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="creator",
        blank=False,
        null=False,
        help_text="The creator of the quiz")

    objects = CategoryManager()

    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"
        unique_together=('category', 'creator')

    def __unicode__(self):
        return self.category