# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0002_auto_20150628_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='launch_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
    ]
