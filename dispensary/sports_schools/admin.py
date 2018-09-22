from django.contrib import admin

from .models import Coach
from .models import SportsSchool


@admin.register(SportsSchool)
class SportsSchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'phone_no')
    search_fields = ('name', 'city__name', 'phone_no')
    list_filter = ('city', )


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_no', 'sports_school__name')
    list_filter = ('sex', 'sports_school')
