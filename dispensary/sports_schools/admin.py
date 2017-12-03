from django.contrib import admin

from .models import Coach
from .models import SportsSchool


@admin.register(SportsSchool)
class SportsSchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    pass
