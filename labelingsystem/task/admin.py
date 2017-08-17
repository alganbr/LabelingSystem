from django.contrib import admin

from .models import Task, Participation

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
	list_display = ('title', 'prerequisite', 'creator')
	filter_horizontal = ('label_list', 'post_list', )
	search_fields = ('title', )

admin.site.register(Task, TaskAdmin)

class ParticipationAdmin(admin.ModelAdmin):
	list_display = ('task', 'coder', )
	list_filter = ('task', 'coder', )
	search_fields = ('task', 'coder', )

admin.site.register(Participation, ParticipationAdmin)