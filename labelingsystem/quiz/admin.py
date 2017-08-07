# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http import HttpResponseRedirect

from .models import *
from category.models import Category
from question.models import Question

# Register your models here.

class QuizAdmin(admin.ModelAdmin):
	admin_fields = ('title', 'description', 'category', 'max_questions', 'pass_mark', 'random_order', 'single_attempt', 'question_list', )
	superuser_fields = ('creator', )
	list_display = ('title', 'category', 'creator', )
	list_filter = ('category', )
	filter_horizontal = ('question_list', )
	search_fields = ('description', 'category__category', )
	actions = ['send_quiz']

	def render_change_form(self, request, context, *args, **kwargs):
		if not request.user.is_superuser:
			context['adminform'].form.fields['category'].queryset = Category.objects.filter(creator=request.user.pk)
			context['adminform'].form.fields['question_list'].queryset = Question.objects.filter(creator=request.user.pk)
		return super(QuizAdmin, self).render_change_form(request, context, *args, **kwargs)

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.fields = self.admin_fields + self.superuser_fields
		else:
			self.fields = self.admin_fields

		return super(QuizAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			obj.creator = request.user
		super(QuizAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(QuizAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creator=request.user)

	def send_quiz(self, request, queryset):
		selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
		return HttpResponseRedirect('/quiz/send_quiz/?ids=%s' % (','.join(selected)))
	send_quiz.short_description = "Send selected quizzes"

admin.site.register(Quiz, QuizAdmin)
