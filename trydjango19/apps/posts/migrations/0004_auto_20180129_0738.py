# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-29 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180126_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='posts',
            name='publish',
            field=models.DateField(null=True),
        ),
    ]
