# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile_no',
            field=models.BigIntegerField(max_length=12),
        ),
    ]
