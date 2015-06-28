# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0006_auto_20150628_2154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='MovieUser',
            new_name='user',
        ),
    ]
