# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-29 21:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0007_auto_20170723_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitionsGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Competition',
        ),
        migrations.AlterField(
            model_name='groupevent',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.CompetitionsGenre'),
        ),
        migrations.AlterField(
            model_name='individualevent',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='competitions.CompetitionsGenre'),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
