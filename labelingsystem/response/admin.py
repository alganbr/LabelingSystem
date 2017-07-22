# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from response.models import QuizResponse, QuestionResponse

# Register your models here.
class QuizResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'quiz', 'score', 'created_at')
	list_filter = ('user', 'quiz', 'score', )
	search_fields = ('user', 'quiz', )
admin.site.register(QuizResponse, QuizResponseAdmin)

class QuestionResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'question', 'correct', 'created_at')
	list_filter = ('user', 'question', 'correct', )
	search_fields = ('user', 'question', )
admin.site.register(QuestionResponse, QuestionResponseAdmin)