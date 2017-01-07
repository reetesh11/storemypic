from __future__ import unicode_literals
from django.core.files.base import ContentFile
from django.conf import settings
from django.db import models
from PIL import Image
import boto
import uuid
import os
from django.utils.deconstruct import deconstructible
from storages.backends.s3boto import S3BotoStorage
from StringIO import StringIO


def get_path_for_my_model_file(instance, filename):
    return path_and_rename('photo/', filename)

def path_and_rename(prefix, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex, ext)
    return os.path.join(prefix, filename)

class Photo(models.Model):
    name  = models.CharField(max_length=100, null=True, blank=True, unique=True, editable=False)
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, default=False, max_length=4000,
                              upload_to=get_path_for_my_model_file)
    thumbnail = models.ImageField(null=True, editable=False, max_length=4000,
                                  upload_to='thumbnail/')
    
    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        super(Photo, self).save(force_insert, force_update)
        thumbnail = StringIO()
        self.name = str(self.photo)
        if self.photo:
            im = Image.open(self.photo)
            if im.size > settings.IMAGE_MAX_SIZE:
                im.thumbnail(settings.IMAGE_MAX_SIZE)     
                im.save(thumbnail, im.format)
                self.photo.save(self.photo.name, ContentFile(thumbnail.getvalue()))
            super(Photo, self).save(force_insert, force_update)
        if self.thumbnail:
            if isinstance(StringIO, self.thumbnail):
                self.thumbnail.save(self.photo.name, ContentFile(self.thumbnail.getvalue()))
            super(Photo, self).save(force_insert, force_update)

    class Meta:
        db_table = "photo"
        ordering = ["-created_at"]
