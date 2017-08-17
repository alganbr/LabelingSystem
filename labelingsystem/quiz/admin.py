from django.contrib import admin

from .models import Quiz, Answer, AnswerKey

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
	list_display = ('title', 'creator', )
	filter_horizontal = ('label_list', 'post_list')
	search_fields = ('title', )

admin.site.register(Quiz, QuizAdmin)

class AnswerInline(admin.TabularInline):
	model = Answer

class AnswerKeyAdmin(admin.ModelAdmin):
	list_display = ('quiz', )
	inlines = [AnswerInline, ]

admin.site.register(AnswerKey, AnswerKeyAdmin)