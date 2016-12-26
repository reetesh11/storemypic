from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from PIL import Image
import boto

class Photo(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, default=False, upload_to='photo')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "photo"
        ordering = ["-created_at"]

    def save(self, force_insert=False, force_update=False):
        super(Photo, self).save(force_insert, force_update)
        if self.photo:
            im = Image.open(self.photo)
            bucket = self.connect_bucket()
            if im.size > settings.IMAGE_MAX_SIZE:
                im.thumbnail(settings.IMAGE_MAX_SIZE)
                im.save()
            # import pdb; pdb.set_trace()
            # if im.size > settings.THUMBNAIL_SIZE:
            #     im.thumbnail(settings.THUMBNAIL_SIZE)
            #     thumbnail = ThumbNail(thumbnail=self.resize_photo(im, settings.THUMBNAIL_SIZE),
            #                           photo=self)
            #     thumbnail.save()
            super(Photo, self).save(force_insert, force_update)

    def resize_photo(self, image, size):
        image.thumbnail(size)
        return image

    def connect_bucket(self):
        conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        return conn.get_bucket(settings.AWS_BUCKET_NAME)

class ThumbNail(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnail")
    photo = models.ForeignKey(Photo)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    class Meta:
        db_table = "thumbnail"
        ordering = ["-created_at"]
