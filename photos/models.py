from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from PIL import Image
import boto

class Photo(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, default=False, upload_to='photo')
    thumbnail = models.ImageField(upload_to="thumbnail", editable=False, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "photo"
        ordering = ["-created_at"]

    def save(self, force_insert=False, force_update=False):
        super(Photo, self).save(force_insert, force_update)
        if self.photo:
            im = Image.open(self.photo)
            if im.size > settings.IMAGE_MAX_SIZE:
                im.thumbnail(settings.IMAGE_MAX_SIZE)
                self.photo = im
            super(Photo, self).save(force_insert, force_update)

class Thumbnail(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnail")
    #photo = models.ForeignKey(Photo)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    class Meta:
        db_table = "thumbnail"
        ordering = ["-created_at"]

    def save(self, force_insert=False, force_update=False):
        super(Thumbnail, self).save(force_insert, force_update)
        im = Image.open(self.thumbnail)
        
