# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Companies', '0002_auto_20180209_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='truck_id',
            field=models.IntegerField(default=-1),
        ),
    ]
