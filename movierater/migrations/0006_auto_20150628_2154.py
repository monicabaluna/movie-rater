# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0005_auto_20150628_2110'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MovieUser',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='user',
            new_name='MovieUser',
        ),
    ]
