# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_auto_20160617_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]