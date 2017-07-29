# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-29 20:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pronites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pronitesevent',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='pronites.PronitesGenre'),
        ),
    ]
