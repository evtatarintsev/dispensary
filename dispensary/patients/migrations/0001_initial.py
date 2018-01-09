# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reference_books', '0001_initial'),
        ('sports_schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(db_index=True, max_length=150, verbose_name='ФИО')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('sex', models.PositiveIntegerField(choices=[(0, 'Мужской'), (1, 'Женский')], default=0, verbose_name='Пол')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('phone_no', models.CharField(blank=True, max_length=50, null=True, verbose_name='Телефон')),
                ('education', models.CharField(blank=True, max_length=150, null=True, verbose_name='Образование')),
                ('training_from_year', models.PositiveIntegerField(blank=True, null=True, verbose_name='С какого года тренируется')),
                ('umo', models.DateField(blank=True, null=True, verbose_name='Дата УМО')),
                ('umo_comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий УМО')),
                ('umo_limit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Допуск УМО')),
                ('emo', models.DateField(blank=True, null=True, verbose_name='Дата ЭМО')),
                ('emo_comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='Комментарий ЭМО')),
                ('emo_limit', models.CharField(blank=True, max_length=255, null=True, verbose_name='Допуск ЭМО')),
                ('work', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место работы')),
                ('profession', models.CharField(blank=True, max_length=255, null=True, verbose_name='Профессия')),
                ('polyclinic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Поликлиника по месту жительства')),
                ('alcohol', models.CharField(blank=True, choices=[('случайное', 'случайное'), ('мало', 'мало'), ('много', 'много'), ('часто', 'часто'), ('не употребляет', 'не употребляет')], max_length=255, null=True, verbose_name='Употребление алкоголя')),
                ('smoking', models.CharField(blank=True, max_length=255, null=True, verbose_name='Курение')),
                ('disease', models.CharField(blank=True, max_length=255, null=True, verbose_name='Болезни')),
                ('injuries', models.CharField(blank=True, max_length=255, null=True, verbose_name='Травмы')),
                ('operations', models.CharField(blank=True, max_length=255, null=True, verbose_name='Болезни')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('coaches', models.ManyToManyField(blank=True, null=True, to='sports_schools.Coach', verbose_name='Тренера')),
                ('food_regime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference_books.FoodRegime', verbose_name='Пищевой режим')),
                ('housing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='reference_books.Housing', verbose_name='Жилищные условия')),
                ('other_sports', models.ManyToManyField(blank=True, help_text='Какими другими видами спорта занимался', related_name='_patient_other_sports_+', to='reference_books.Sport', verbose_name='Другие виды спорта')),
                ('rank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='reference_books.Rank', verbose_name='Разряд')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='reference_books.Sport', verbose_name='Вид спорта')),
                ('sports_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to='sports_schools.SportsSchool', verbose_name='Организация')),
                ('tournament_sports', models.ManyToManyField(blank=True, help_text='По каким видам спорта участвовал в соревнованиях', to='reference_books.Sport', verbose_name='Другие виды спорта')),
                ('training_stage', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='reference_books.TrainingStage', verbose_name='Этап подготовки')),
            ],
            options={
                'verbose_name_plural': 'Пациенты',
                'verbose_name': 'Пациент',
            },
        ),
    ]