# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0002_stringset'),
    ]

    operations = [
        migrations.AddField(
            model_name='stringset',
            name='name',
            field=models.CharField(default='x', max_length=128),
            preserve_default=False,
        ),
    ]
