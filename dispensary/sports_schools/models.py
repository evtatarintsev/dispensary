from django.db import models

from dispensary.reference_books.models import City
from dispensary.reference_books.models import SEX_CHOICES
from dispensary.reference_books.models import MALE


class SportsSchool(models.Model):
    name = models.CharField('Название', max_length=255)
    city = models.ForeignKey(City, verbose_name='Город', null=True, on_delete=models.SET_NULL)
    phone_no = models.CharField('Контактный телефон', max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Спортшкола'
        verbose_name_plural = 'Спортшколы'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Coach(models.Model):
    sports_school = models.ForeignKey(SportsSchool, verbose_name='Организация', related_name='coaches',
                                      null=True, blank=True)
    full_name = models.CharField('ФИО', max_length=150, db_index=True)
    sex = models.PositiveIntegerField('Пол', choices=SEX_CHOICES, default=MALE)

    birthday = models.DateField('Дата рождения', null=True, blank=True)
    phone_no = models.CharField('Телефон', max_length=50, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
        ordering = ['full_name', ]

    def __str__(self):
        return self.full_name
