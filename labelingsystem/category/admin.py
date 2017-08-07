# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	admin_fields = ('category', )
	superuser_fields = ('creator', )
	search_fields = ('category', )

	def get_form(self, request, obj=None, **kwargs):
		if request.user.is_superuser:
			self.fields = self.admin_fields + self.superuser_fields
		else:
			self.fields = self.admin_fields
		return super(CategoryAdmin, self).get_form(request, obj, **kwargs)

	def save_model(self, request, obj, form, change):
		if not request.user.is_superuser:
			obj.creator = request.user
		super(CategoryAdmin, self).save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super(CategoryAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(creator=request.user)

admin.site.register(Category, CategoryAdmin)