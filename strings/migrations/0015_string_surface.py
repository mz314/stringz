# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0014_auto_20160610_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='string',
            name='surface',
            field=models.CharField(default='p', max_length=128),
            preserve_default=False,
        ),
    ]
