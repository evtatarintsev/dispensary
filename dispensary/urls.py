from django.conf.urls import url
from django.contrib import admin


admin.site.site_title = 'Кировский спортивный диспансер'
admin.site.site_header = 'Кировский спортивный диспансер'


urlpatterns = [
    url(r'^', admin.site.urls),
]
