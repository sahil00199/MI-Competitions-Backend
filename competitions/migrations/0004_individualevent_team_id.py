# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-22 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_auto_20170627_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='individualevent',
            name='team_id',
            field=models.IntegerField(default=0),
        ),
    ]
