# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-29 12:51
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0009_auto_20180629_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='user_pic',
        ),
        migrations.AddField(
            model_name='bio',
            name='user_upic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
