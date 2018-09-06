from django.contrib import admin
from .models import Post, Category, Tag, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', "starter_image_post", 'author','video_file', 'status', 'category', 'link')
    search_fields = ['title', 'content']
    ordering = ['-published_at', 'status']
    list_filter = ['published_at']
    date_hierarchy = 'published_at'
    filter_horizontal = ('tags',)
    raw_id_fields = ('tags',)
   #prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('slug',)
    fields = ('title', 'slug', 'status','content', 'author', 'category',
              'tags', 'video_file', 'starter_image_post','link_starter_image', 'link')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'starter_image_cat')
    search_fields = ('name',)
    readonly_fields = ('slug',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    readonly_fields = ('slug',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'post', 'created_date', 'approved_comment')
    list_filter = ('approved_comment', 'created_date', 'updated_date')
    search_field = ('author', 'email', 'text')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)