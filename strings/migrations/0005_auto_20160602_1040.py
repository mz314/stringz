# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0004_auto_20160502_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='string',
            old_name='gauge_inch',
            new_name='gauge_imperial',
        ),
    ]
