# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-25 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20180113_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='team_member',
            field=models.BooleanField(default=False, verbose_name='Член сборной'),
        ),
    ]
