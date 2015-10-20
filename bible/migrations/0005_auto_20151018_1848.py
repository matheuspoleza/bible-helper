# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0004_book_testament'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='cod',
            field=models.CharField(default='gn', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='short_name',
            field=models.CharField(max_length=2),
        ),
    ]
