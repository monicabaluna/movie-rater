# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, unique=True, max_length=100)),
                ('launch_date', models.DateTimeField(null=True)),
                ('imdb_link', models.URLField(max_length=100)),
                ('poster', models.CharField(max_length=1000, default='https://nanohub.org/groups/bnc/Image:/equipment/missing_equip.gif')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, unique=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('grade', models.IntegerField(default=5)),
                ('movie', models.ForeignKey(to='movierater.Movie', related_name='votes')),
                ('user', models.ForeignKey(to='movierater.User', related_name='votes')),
            ],
        ),
    ]
