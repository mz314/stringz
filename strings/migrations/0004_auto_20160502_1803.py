# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0003_stringset_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='string',
            old_name='gauge',
            new_name='gauge_inch',
        ),
    ]
