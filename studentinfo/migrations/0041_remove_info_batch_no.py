# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-22 07:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0040_info_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='batch_no',
        ),
    ]
