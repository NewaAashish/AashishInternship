# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-03 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0019_auto_20190703_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
