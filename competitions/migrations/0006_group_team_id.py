# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0005_auto_20170722_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='team_id',
            field=models.IntegerField(default=0),
        ),
    ]
