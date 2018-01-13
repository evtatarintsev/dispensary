from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin


admin.site.site_title = 'Кировский спортивный диспансер'
admin.site.site_header = 'Кировский спортивный диспансер'


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^', admin.site.urls),
    url(r'^admin/salmonella/', include('salmonella.urls')),
]
