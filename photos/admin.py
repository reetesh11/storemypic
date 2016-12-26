from django.contrib import admin
from photos.models import Photo, Thumbnail

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "thumbnail", "created_at"]

    class Meta:
        model = Photo

class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ["thumbnail", "created_at"]

    class Meta:
        model = Thumbnail

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Thumbnail, ThumbnailAdmin)

