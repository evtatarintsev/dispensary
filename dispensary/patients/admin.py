from django.contrib import admin
from salmonella.admin import SalmonellaMixin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(SalmonellaMixin, admin.ModelAdmin):
    # change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ('full_name', 'sport', 'sports_school', 'umo', 'umo_limit', 'emo', 'emo_limit',)

    search_fields = ('full_name', 'sports_school__name')
    salmonella_fields = ('coaches',)
    list_filter = ('sports_school', 'sport', 'rank', )
    readonly_fields = ('umo_comment', 'emo_comment',)
    fieldsets = (
        ('Общая информация', ({'fields': (
            'full_name', 'sex', 'birthday', 'address', 'phone_no',
        ),
        'classes': ('grp-collapse grp-closed',)}),),
        ('Спортивная информация', ({'fields': (
            'sports_school', 'sport', 'coaches', 'rank', 'training_from_year', 'training_stage',
        )}),),
        ('Допуски', ({'fields': (
            ('umo', 'umo_comment'), 'umo_limit', ('emo', 'emo_comment'), 'emo_limit',
        )}),),
    )
