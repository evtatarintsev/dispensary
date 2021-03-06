# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 14:53
from __future__ import unicode_literals
from datetime import datetime
from django.db import migrations


def migrate_bd(apps, schema_editor):
    Patient = apps.get_model('patients.Patient')
    count = 0
    for p in Patient.objects.filter(birthday=None):
        try:
            p.birthday = datetime.strptime(p.birthday_str, '%d.%m.%Y')
            p.save()
            count += 1
        except:
            try:
                p.birthday = datetime.strptime(p.birthday_str, '%d.%m.%y')
                p.save()
                count += 1
            except:
                print(p.birthday_str, 'fail')

    print('Updated %s records' % count)


def reverse_bd(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20171202_1041'),
    ]

    operations = [
        migrations.RunPython(migrate_bd, reverse_bd),
    ]
