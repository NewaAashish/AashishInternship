# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-06-26 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0017_auto_20190626_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='avg',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
