# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from response.models import QuizResponse, QuizQuestionResponse
from django.utils.safestring import mark_safe

# Register your models here.
class QuizResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'quiz', 'score', 'created_at', 'detail')
	list_filter = ('user', 'quiz', 'score', )
	search_fields = ('user', 'quiz', )

	def detail(self, obj):
		url_string = """<a href="/response/quiz_response_detail/{0}">Detail</a>""".format(obj.id)
		return  mark_safe(url_string)

admin.site.register(QuizResponse, QuizResponseAdmin)

class QuizQuestionResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'question', 'correct', 'created_at')
	list_filter = ('user', 'question', 'correct', )
	search_fields = ('user', 'question', )
admin.site.register(QuizQuestionResponse, QuizQuestionResponseAdmin)