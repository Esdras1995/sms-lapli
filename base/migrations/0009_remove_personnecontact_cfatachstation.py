# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20151004_0851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnecontact',
            name='cfAtachStation',
        ),
    ]
