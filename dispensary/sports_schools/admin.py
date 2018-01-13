from django.contrib import admin

from .models import Coach
from .models import SportsSchool


@admin.register(SportsSchool)
class SportsSchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_no', 'sports_school__name')
    list_filter = ('sex', 'sports_school')
