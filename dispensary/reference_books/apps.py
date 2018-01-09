from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ReferenceBooksConfig(AppConfig):
    name = 'dispensary.reference_books'
    verbose_name = _('Справочники')


default_app_config = '{module}.{app}'.format(
    module=__name__,
    app=ReferenceBooksConfig.__name__
)
