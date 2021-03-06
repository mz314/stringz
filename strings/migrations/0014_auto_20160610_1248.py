# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-10 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0013_string_unit_weight_imperial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScaleLength',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale_imperial', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='stringset',
            name='scale_lengths',
            field=models.ManyToManyField(to='strings.ScaleLength'),
        ),
    ]
