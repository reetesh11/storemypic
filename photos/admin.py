from django.contrib import admin
from photos.models import Photo, ThumbNail

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

    class Meta:
        model = Photo

class ThumbNailAdmin(admin.ModelAdmin):
    list_display = ["thumbnail", "created_at"]

    class Meta:
        model = ThumbNail

admin.site.register(Photo, PhotoAdmin)
admin.site.register(ThumbNail, ThumbNailAdmin)

