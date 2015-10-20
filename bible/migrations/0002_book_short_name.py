# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='short_name',
            field=models.CharField(default='Gen', max_length=3),
            preserve_default=False,
        ),
    ]
