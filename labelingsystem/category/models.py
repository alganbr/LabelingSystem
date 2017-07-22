# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

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
        unique=True,
        null=True)

    objects = CategoryManager()

    class Meta:
        verbose_name="category"
        verbose_name_plural="categories"

    def __unicode__(self):
        return self.category