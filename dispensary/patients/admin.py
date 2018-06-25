from django.contrib import admin
from salmonella.admin import SalmonellaMixin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(SalmonellaMixin, admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ('full_name', 'birthday_short', 'sport', 'team_member', 'sports_school', 'umo', 'umo_limit', 'emo', 'emo_limit',)
    list_editable = ('team_member', )
    search_fields = ('full_name', 'sports_school__name')
    salmonella_fields = ('coaches',)
    list_filter = ('sports_school', 'sport', 'rank', 'team_member', 'coaches')
    readonly_fields = ('umo_comment', 'emo_comment',)
    fieldsets = (
        ('Общая информация', ({'fields': (
            'full_name', 'sex', 'birthday', 'address', 'phone_no',
        ),
        }),),
        ('Спортивная информация', ({'fields': (
            'sports_school', 'sport', 'coaches', 'rank', 'training_from_year', 'training_stage', 'team_member'
        )}),),
        ('Допуски', ({'fields': (
            ('umo', 'umo_comment'), 'umo_limit', 'recommendations', ('emo', 'emo_comment'), 'emo_limit',
        )}),),
    )

    def birthday_short(self, obj):
        return obj.birthday.strftime('%d.%m.%Y') if obj.birthday else None
    birthday_short.short_description = 'Д/Р'
    birthday_short.admin_order_field = 'birthday'
