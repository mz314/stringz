# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('strings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StringSet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('strings', models.ManyToManyField(to='strings.String')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
