# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbNail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
            ],
        ),
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='thumbnail',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Photo'),
        ),
    ]
