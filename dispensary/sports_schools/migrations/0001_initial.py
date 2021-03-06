# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=150, verbose_name='ФИО')),
                ('sex', models.PositiveIntegerField(choices=[(0, 'Мужской'), (1, 'Женский')], default=0, verbose_name='Пол')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='SportsSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Контактный телефон')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reference_books.City', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Спортшкола',
                'verbose_name_plural': 'Спортшколы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='coach',
            name='sports_school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='sports_schools.SportsSchool', verbose_name='Организация'),
        ),
    ]
