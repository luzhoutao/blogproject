from django.contrib import admin
from iblog.models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'auth']
# Register your models here.

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
