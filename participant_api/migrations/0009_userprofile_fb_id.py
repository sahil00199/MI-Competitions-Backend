# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant_api', '0008_auto_20170726_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='fb_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]