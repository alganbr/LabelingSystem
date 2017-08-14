from django.contrib import admin

from .models import Post, PostResponse

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('content', 'author', )
	search_fields = ('content', 'author', )

admin.site.register(Post, PostAdmin)

class PostResponseAdmin(admin.ModelAdmin):
	list_display = ('responder', 'post', 'timestamp', )
	list_filter = ('responder', 'post', )
	search_fields = ('responder', 'post', )

admin.site.register(PostResponse, PostResponseAdmin)