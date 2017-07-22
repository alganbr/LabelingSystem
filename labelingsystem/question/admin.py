# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from answer.admin import AnswerInline

from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('content', 'category', )
	list_filter = ('category', )
	fields = ('content', 'category', 'explanation', )
	search_fields = ('content', 'explanation', )
	inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)