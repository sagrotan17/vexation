from django.contrib import admin
from .models import Category, Tag, Gallery, Photo


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "is_public", "starter_image", "created_date")
    search_fields = ('title',)
    readonly_fields = ('slug',)


    class Meta:
        model = Gallery

class PhotoAdmin(admin.ModelAdmin):
    list_display = ("title", "width", "height", "gallery", "is_public", "timestamp", "landscape_format")
    search_fields = ('title',)

    class Meta:
        model = Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ('name',)
    readonly_fields = ('slug',)

    class Meta:
        model = Category

class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ('name',)
    readonly_fields = ('slug',)

    class Meta:
        model = Tag


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)