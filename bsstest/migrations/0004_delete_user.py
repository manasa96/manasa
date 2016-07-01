# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsstest', '0003_auto_20160622_0857'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
