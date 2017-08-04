# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	admin_fields = ('title', 'description', 'category', 'max_questions', 'question_list', )
	superuser_fields = ('creator', )
	list_display = ('title', 'category', 'creator', )
	list_filter = ('category', )
	filter_horizontal = ('question_list', )
	search_fields = ('description', 'category', )

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.fields = self.admin_fields + self.superuser_fields
		else:
			self.fields = self.admin_fields
		return super(TaskAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			obj.creator = request.user
		super(TaskAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(TaskAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creator=request.user)

admin.site.register(Task, TaskAdmin)