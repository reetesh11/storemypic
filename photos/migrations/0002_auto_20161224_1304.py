# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(default=False, upload_to='photo')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'photo',
            },
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
