# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from answer.admin import AnswerInline

from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
	admin_fields = ('category', 'content', 'explanation', )
	superuser_fields = ('creator', )
	list_display = ('content', 'category', )
	list_filter = ('category', )
	fields = ('content', 'category', 'explanation', )
	search_fields = ('content', 'explanation', )
	inlines = [AnswerInline]

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.fields = self.admin_fields + self.superuser_fields
		else:
			self.fields = self.admin_fields
		return super(QuestionAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			obj.creator = request.user
		super(QuestionAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(QuestionAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creator=request.user)

admin.site.register(Question, QuestionAdmin)