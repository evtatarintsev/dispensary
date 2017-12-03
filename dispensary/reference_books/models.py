from django.db import models

MALE = 0
FEMALE = 1

SEX_CHOICES = (
    (MALE, 'Мужской'),
    (FEMALE, 'Женский'),
)


class Housing(models.Model):
    name = models.CharField('Название', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Жилищные условия'
        verbose_name_plural = 'Жилищные условия'
        ordering = ['position', ]

    def __str__(self):
        return self.name


class FoodRegime(models.Model):
    name = models.CharField('Название', max_length=255)
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Пищевой режим'
        verbose_name_plural = 'Пищевой режим'
        ordering = ['position', ]

    def __str__(self):
        return self.name


class Sport(models.Model):
    name = models.CharField('Название', max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Вид спорта'
        verbose_name_plural = 'Виды спорта'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField('Название', max_length=50)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name


class TrainingStage(models.Model):
    name = models.CharField('Название', max_length=50)
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Этап подготовки'
        verbose_name_plural = 'Этапы подготовки'
        ordering = ['position', ]

    def __str__(self):
        return self.name


class Rank(models.Model):
    name = models.CharField('Название', max_length=50)
    position = models.PositiveIntegerField('Позиция', default=0)

    class Meta:
        verbose_name = 'Разряд'
        verbose_name_plural = 'Разряды'
        ordering = ['position', ]

    def __str__(self):
        return self.name

