# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-02-17 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
