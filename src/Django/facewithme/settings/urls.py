from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from apps.core.views import HomePageView, GeoIPView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^amf/', 'apps.core.amfgateway.services', name = 'core:amfservices'),
    url(r'^geoip.js$', GeoIPView.as_view(), name = 'core:geoip'),
    url(r'^$', HomePageView.as_view(), name = 'core:homepageview'),
    url(r'^stream/', include('apps.core.urls', namespace='core')),
)

#urlpatterns += patterns('apps.core.views',
#    
#)
