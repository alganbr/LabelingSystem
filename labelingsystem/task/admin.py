# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'creator', )
	list_filter = ('category', )
	filter_horizontal = ('question_list', )
	search_fields = ('description', 'category', )
admin.site.register(Task, TaskAdmin)