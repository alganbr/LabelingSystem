from django.contrib import admin

from .models import Quiz, Answer, AnswerKey, QuizResponse

# Register your models here.
class QuizAdmin(admin.ModelAdmin):
	list_display = ('title', 'creator', )
	filter_horizontal = ('label_list', 'post_list')
	search_fields = ('title', )

admin.site.register(Quiz, QuizAdmin)

# class AnswerAdmin(admin.ModelAdmin):
# 	list_display = ('quiz', 'post', 'label', )
# 	list_filter = ('quiz', 'post', )
# 	search_fields = ('quiz', 'post', )

# admin.site.register(Answer, AnswerAdmin)

class AnswerInline(admin.TabularInline):
	model = Answer

class AnswerKeyAdmin(admin.ModelAdmin):
	list_display = ('quiz', )
	inlines = [AnswerInline, ]

admin.site.register(AnswerKey, AnswerKeyAdmin)

class QuizResponseAdmin(admin.ModelAdmin):
	list_display = ('responder', 'quiz', 'score', 'timestamp', )
	list_filter = ('responder', 'quiz', 'score')
	search_fields = ('responder', 'quiz', )

admin.site.register(QuizResponse, QuizResponseAdmin)