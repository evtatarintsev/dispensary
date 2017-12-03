from django.contrib import admin

from .models import Housing
from .models import FoodRegime
from .models import Sport
from .models import City
from .models import TrainingStage
from .models import Rank


@admin.register(FoodRegime)
class FoodRegimeAdmin(admin.ModelAdmin):
    pass


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    pass


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(TrainingStage)
class TrainingStageAdmin(admin.ModelAdmin):
    pass


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    pass
