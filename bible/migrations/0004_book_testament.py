# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0003_auto_20151017_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='testament',
            field=models.CharField(default='old', max_length=3, choices=[(b'old', b'Velho Testamento'), (b'new', b'Novo Testamento')]),
            preserve_default=False,
        ),
    ]
