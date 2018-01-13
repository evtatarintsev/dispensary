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
                                          null=True, blank=True, choices=YEARS)

    umo = models.DateField('Дата УМО', null=True, blank=True)
    umo_comment = models.CharField('Комментарий УМО', max_length=255, null=True, blank=True)
    umo_limit = models.TextField('Допуск УМО', max_length=255, null=True, blank=True)

    emo = models.DateField('Дата ЭМО', null=True, blank=True)
    emo_comment = models.CharField('Комментарий ЭМО', max_length=255, null=True, blank=True)
    emo_limit = models.TextField('Допуск ЭМО', max_length=255, null=True, blank=True)

    # other_sports = models.ManyToManyField(Sport, verbose_name='Другие виды спорта', related_name='+', blank=True,
    #                                       help_text='Какими другими видами спорта занимался')
    # tournament_sports = models.ManyToManyField(Sport, verbose_name='Соревнования', blank=True,
    #                                            help_text='По каким видам спорта участвовал в соревнованиях')
    # education = models.CharField('Образование', max_length=150, null=True, blank=True)
    # housing = models.ForeignKey(Housing, verbose_name='Жилищные условия',
    #                             null=True, blank=True, on_delete=models.SET_NULL)
    # food_regime = models.ForeignKey(FoodRegime, verbose_name='Пищевой режим',
    #                                 null=True, blank=True, on_delete=models.SET_NULL)

    # work = models.CharField('Место работы', max_length=255, null=True, blank=True)
    # profession = models.CharField('Профессия', max_length=255, null=True, blank=True)
    # polyclinic = models.CharField('Поликлиника по месту жительства', max_length=255, null=True, blank=True)
    # alcohol = models.CharField('Употребление алкоголя', max_length=255, choices=ALCOHOL, null=True, blank=True)
    # smoking = models.CharField('Курение', max_length=255, null=True, blank=True)

    # disease = models.CharField('Болезни', max_length=255, null=True, blank=True)
    # injuries = models.CharField('Травмы', max_length=255, null=True, blank=True)
    # operations = models.CharField('Болезни', max_length=255, null=True, blank=True)

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
