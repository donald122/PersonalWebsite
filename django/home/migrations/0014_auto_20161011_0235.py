# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 02:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_experience_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='location',
            new_name='locations',
        ),
    ]