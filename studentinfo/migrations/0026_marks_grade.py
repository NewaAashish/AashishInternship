# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-04 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0025_remove_marks_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='grade',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
