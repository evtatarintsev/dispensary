from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'sport', 'sports_school', 'rank', 'training_stage', 'birthday_str')
    search_fields = ('full_name', 'sports_school__name')
    filter_horizontal = ('coaches', 'other_sports', 'tournament_sports')
    list_filter = ('rank', )

    def get_queryset(self, request):
        return super(PatientAdmin, self).get_queryset(request).select_related()
