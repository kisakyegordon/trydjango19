# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-26 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
