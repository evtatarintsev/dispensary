import csv
from datetime import datetime
from django.core.management import BaseCommand


from dispensary.patients.models import Patient
from dispensary.sports_schools.models import SportsSchool
from dispensary.sports_schools.models import Coach
from dispensary.reference_books.models import Housing
from dispensary.reference_books.models import FoodRegime
from dispensary.reference_books.models import Sport
from dispensary.reference_books.models import TrainingStage
from dispensary.reference_books.models import Rank


fieldnames = [
    'number',
    'org',
    'sport',
    'podg',
    'rank',
    'fio',
    'bd',
    'sex',
    'address',
    'phone',

    'coach',
    'edu',
    'zilishe',
    'eda',
    'sport',
    'training_from',
    'other_sports',
    'tournir',
    'umo',
    'umo_dopusk',
    'emo',
    'emo_dopusk',
    'work',
    'profession',

    'policlinika',
    'alcohol',
    'smoking',
    'bolesni',
    'travmy',
    'operation',
    'a1',
    'a2',
    'a3',
    'a4',
    'a5',
]


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        fname = options['filename']
        content = open(fname, encoding='cp1251')
        dialect = csv.excel
        dialect.delimiter = ';'
        reader = csv.DictReader(content, fieldnames, dialect=dialect)
        next(reader)
        next(reader)

        for row in reader:
            school, _ = SportsSchool.objects.get_or_create(name=row['org'])
            coach, _ = Coach.objects.get_or_create(full_name=row['coach'])
            rank, _ = Rank.objects.get_or_create(name=row['rank'])
            training_stage, _ = TrainingStage.objects.get_or_create(name=row['podg'])
            sport, _ = Sport.objects.get_or_create(name=row['sport'])
            housing, _ = Housing.objects.get_or_create(name=row['zilishe'])
            food_regime, _ = FoodRegime.objects.get_or_create(name=row['eda'])

            umo_comment = None
            umo = None
            try:
                umo = datetime.strptime(row['umo'], '%d.%m.%Y')
            except:
                umo_comment = row['umo']

            emo_comment = None
            emo = None
            try:
                emo = datetime.strptime(row['emo'], '%d.%m.%Y')
            except:
                try:
                    emo = datetime.strptime(row['emo'], '%d.%m.%y')
                except:
                    emo_comment = row['umo']

            p = Patient.objects.create(
                sports_school=school,
                sport=sport,
                training_stage=training_stage,
                rank=rank,
                full_name=row['fio'],
                birthday_str=row['bd'],
                sex=1 if row['sex'] == 'женский' else 0,
                address=row['address'],
                phone_no=row['phone'],
                education=row['edu'],
                housing=housing,
                food_regime=food_regime,
                training_from_year=row['training_from'],
                umo=umo,
                umo_comment=umo_comment,
                umo_limit=row['umo_dopusk'],
                emo=emo,
                emo_comment=emo_comment,
                emo_limit=row['emo_dopusk'],
                work=row['work'],
                profession=row['profession'],
                polyclinic=row['policlinika'],
                alcohol=row['alcohol'],
                smoking=row['smoking'],
                disease=row['bolesni'],
                injuries=row['travmy'],
                operations=row['operation'],
            )

            p.coaches.add(coach)


