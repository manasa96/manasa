# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-21 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bsstest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bss',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='bss',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='bss',
            name='occupation',
            field=models.CharField(max_length=30),
        ),
    ]
