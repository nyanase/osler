# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-07-09 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('followup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalgeneralfollowup',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicallabfollowup',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalreferralfollowup',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='historicalvaccinefollowup',
            name='history_change_reason',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
