# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('chapter', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('cod', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='verse',
            name='bible_version',
            field=models.ForeignKey(to='bible.Version'),
        ),
        migrations.AddField(
            model_name='verse',
            name='book',
            field=models.ForeignKey(to='bible.Book'),
        ),
    ]
