# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0002_book_short_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verse',
            name='id',
        ),
        migrations.AddField(
            model_name='verse',
            name='cod',
            field=models.CharField(default='gn11', max_length=5, serialize=False, primary_key=True),
            preserve_default=False,
        ),
    ]
