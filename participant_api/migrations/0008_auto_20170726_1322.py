# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-26 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_api', '0007_auto_20170722_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mi_number',
            field=models.CharField(default='default', max_length=11, unique=True),
        ),
    ]
