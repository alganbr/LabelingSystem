from django.contrib import admin

from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'prerequisite', 'creator')
	filter_horizontal = ('label_list', 'post_list', )
	search_fields = ('title', )

admin.site.register(Task, TaskAdmin)