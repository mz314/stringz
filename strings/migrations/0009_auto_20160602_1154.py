# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-02 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0008_auto_20160602_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='name',
            field=models.CharField(default='x', max_length=16, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='pitch_hz',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=16, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stringstringset',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='strings.Note'),
        ),
    ]
