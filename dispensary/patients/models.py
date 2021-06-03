from django.db import models
from django.utils import timezone

from dispensary.sports_schools.models import SportsSchool
from dispensary.sports_schools.models import Coach
from dispensary.reference_books.models import Rank
from dispensary.reference_books.models import SEX_CHOICES
from dispensary.reference_books.models import MALE
from dispensary.reference_books.models import Housing
from dispensary.reference_books.models import Sport
from dispensary.reference_books.models import FoodRegime
from dispensary.reference_books.models import TrainingStage


ALCOHOL = (
    ('случайное', 'случайное'),
    ('мало', 'мало'),
    ('много', 'много'),
    ('часто', 'часто'),
    ('не употребляет', 'не употребляет'),
)

YEARS_COUNT = 15
YEARS = ((str(i), i) for i in range(timezone.now().year-YEARS_COUNT, timezone.now().year))


class Patient(models.Model):
    sports_school = models.ForeignKey(SportsSchool, verbose_name='Организация', related_name='patients')
    sport = models.ForeignKey(Sport, verbose_name='Вид спорта', related_name='patients',
                              null=True, on_delete=models.SET_NULL)
    training_stage = models.ForeignKey(TrainingStage, verbose_name='Этап подготовки', related_name='patients',
                                       null=True, blank=True, on_delete=models.SET_NULL)
    rank = models.ForeignKey(Rank, verbose_name='Разряд', related_name='patients',
                             null=True, blank=True, on_delete=models.SET_NULL)
    full_name = models.CharField('ФИО', max_length=150, db_index=True)
    birthday = models.DateField('Дата рождения', null=True)
    birthday_str = models.CharField('', max_length=100, null=True, blank=True)
    sex = models.PositiveIntegerField('Пол', choices=SEX_CHOICES, default=MALE)
    address = models.CharField('Адрес', max_length=255, null=True, blank=True)
    phone_no = models.CharField('Телефон', max_length=50, null=True, blank=True)
    coaches = models.ManyToManyField(Coach, verbose_name='Тренера', blank=True)
    training_from_year = models.CharField('С какого года тренируется', max_length=20,
                                          null=True, blank=True)

    umo = models.DateField('Дата УМО', null=True, blank=True)
    umo_number = models.PositiveIntegerField('Номер УМО', default=0)
    umo_comment = models.CharField('Комментарий УМО', max_length=255, null=True, blank=True)
    umo_limit = models.TextField('Допуск УМО', max_length=255, null=True, blank=True)

    emo = models.DateField('Дата ЭМО', null=True, blank=True)
    emo_number = models.PositiveIntegerField('Номер ЭМО', default=0)
    emo_comment = models.CharField('Комментарий ЭМО', max_length=255, null=True, blank=True)
    emo_limit = models.TextField('Допуск ЭМО', max_length=255, null=True, blank=True)

    team_member = models.BooleanField('Член сборной', default=False)
    recommendations = models.TextField('Рекомендации', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    def save(self, **kwargs):
        if self.birthday:
            self.birthday_str = None
        return super(Patient, self).save(**kwargs)

    @property
    def last_name(self):
        return self.split_fio()[0]

    @property
    def first_name(self):
        return self.split_fio()[1]

    @property
    def middle_name(self):
        return self.split_fio()[2]

    def split_fio(self):
        fio = self.full_name.split()
        if len(fio) > 2:
            return fio
        elif len(fio) > 1:
            return fio + ['']
        return fio + ['', '']
