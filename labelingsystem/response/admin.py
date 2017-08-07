# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from response.models import QuizResponse, QuizQuestionResponse, TaskResponse, TaskQuestionResponse
from django.utils.safestring import mark_safe

# Register your models here.
class QuizResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'quiz', 'score', 'created_at', 'sender', 'detail', )
	list_filter = ('user__username', 'quiz__title', 'score', )
	search_fields = ('user__username', 'quiz__title', )

	def get_queryset(self, request):
		qs = super(QuizResponseAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(quiz__creator=request.user)

	def sender(self, obj):
		return obj.quiz.creator

	def detail(self, obj):
		url_string = """<a href="/response/quiz_response_detail/{0}">Detail</a>""".format(obj.id)
		return  mark_safe(url_string)

admin.site.register(QuizResponse, QuizResponseAdmin)

class QuizQuestionResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'question', 'answer', 'correct', 'created_at', )
	list_filter = ('user__username', 'question', 'correct', )
	search_fields = ('user__username', 'question__content', )
admin.site.register(QuizQuestionResponse, QuizQuestionResponseAdmin)

class TaskResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'task', 'created_at', 'sender', 'detail')
	list_filter = ('user__username', 'task__title', )
	search_fields = ('user__username', 'task__title', )

	def get_queryset(self, request):
		qs = super(TaskResponseAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(task__creator=request.user)

	def sender(self, obj):
		return obj.task.creator

	def detail(self, obj):
		url_string = """<a href="/response/task_response_detail/{0}">Detail</a>""".format(obj.id)
		return  mark_safe(url_string)

admin.site.register(TaskResponse, TaskResponseAdmin)

class TaskQuestionResponseAdmin(admin.ModelAdmin):
	list_display = ('user', 'question', 'answer', 'created_at')
	list_filter = ('user__username', 'question', )
	search_fields = ('user__username', 'question__content', )
admin.site.register(TaskQuestionResponse, TaskQuestionResponseAdmin)