from django.contrib import admin
from photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "photo", "thumbnail", "created_at"]

    class Meta:
        model = Photo

admin.site.register(Photo, PhotoAdmin)

