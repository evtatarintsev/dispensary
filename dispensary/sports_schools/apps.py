from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SportsSchoolsConfig(AppConfig):
    name = 'dispensary.sports_schools'
    verbose_name = _('Спортивные школы')


default_app_config = '{module}.{app}'.format(
    module=__name__,
    app=SportsSchoolsConfig.__name__
)
