# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bsstest', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='bss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30, null=True)),
                ('age', models.IntegerField(null=True)),
                ('city', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
            ],
        ),
    ]
