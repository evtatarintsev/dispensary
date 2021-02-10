from django.contrib import admin
from salmonella.admin import SalmonellaMixin
from django.shortcuts import render
from django.conf.urls import url
from .models import Patient


@admin.register(Patient)
class PatientAdmin(SalmonellaMixin, admin.ModelAdmin):
    change_list_template = "admin/change_list_filter_sidebar.html"
    list_display = ('unique_number', 'full_name', 'birthday_short', 'sport', 'team_member',
                    'sports_school', 'umo_display', 'emo_display', 'recommendations')
    list_editable = ('team_member', )
    search_fields = ('pk', 'full_name', 'sports_school__name')
    salmonella_fields = ('coaches',)
    list_filter = ('sports_school', 'sport', 'coaches', 'rank', 'team_member', )
    readonly_fields = ('unique_number', 'umo_comment', 'emo_comment',)
    fieldsets = (
        ('Общая информация', ({'fields': (
            'unique_number', 'full_name', 'sex', 'birthday', 'address', 'phone_no',
        ),
        }),),
        ('Спортивная информация', ({'fields': (
            'sports_school', 'sport', 'coaches', 'rank', 'training_from_year', 'training_stage', 'team_member'
        )}),),
        ('Допуски', ({'fields': (
            ('umo', 'umo_comment'), 'umo_limit', 'recommendations', ('emo', 'emo_comment'), 'emo_limit',
        )}),),
    )

    def unique_number(self, obj):
        return obj.pk
    unique_number.short_description = '№'
    unique_number.admin_order_field = 'pk'

    def birthday_short(self, obj):
        return obj.birthday.strftime('%d.%m.%Y') if obj.birthday else None
    birthday_short.short_description = 'Д/Р'
    birthday_short.admin_order_field = 'birthday'

    def emo_display(self, obj):
        emo_date_str = obj.emo.strftime('%d.%m.%Y') if obj.emo else ''
        data = '<strong>%s</strong><br>%s' % (emo_date_str, obj.emo_limit or '')
        return data

    emo_display.short_description = 'ЭМО'
    emo_display.admin_order_field = 'emo'
    emo_display.allow_tags = True

    def umo_display(self, obj):
        umo_date_str = obj.umo.strftime('%d.%m.%Y') if obj.umo else ''
        umo_limit = obj.umo_limit or 'не указан'
        data = '<strong>%s</strong><br>Допуск: %s' % (umo_date_str, umo_limit)
        return data

    umo_display.short_description = 'УМО'
    umo_display.admin_order_field = 'umo'
    umo_display.allow_tags = True

    def get_urls(self):
        urls = [
            url(r'^analyze/(?P<pk>\d+)/$', self.admin_site.admin_view(self.print_analyze), name='analyze'),
            url(r'^card/(?P<pk>\d+)/$', self.admin_site.admin_view(self.print_card), name='card'),
            url(r'^flu/(?P<pk>\d+)/$', self.admin_site.admin_view(self.print_flu), name='flu'),
            url(r'^label/(?P<pk>\d+)/$', self.admin_site.admin_view(self.print_label), name='label'),
        ] + super(PatientAdmin, self).get_urls()
        return urls

    def print_analyze(self, request, pk):
        return render(request, 'admin/patients/patient/analyze.html', {'obj': Patient.objects.get(pk=pk)})

    def print_card(self, request, pk):
        return render(request, 'admin/patients/patient/card.html', {'obj': Patient.objects.get(pk=pk)})

    def print_flu(self, request, pk):
        return render(request, 'admin/patients/patient/flu.html', {'obj': Patient.objects.get(pk=pk)})

    def print_label(self, request, pk):
        return render(request, 'admin/patients/patient/label.html', {'obj': Patient.objects.get(pk=pk)})
