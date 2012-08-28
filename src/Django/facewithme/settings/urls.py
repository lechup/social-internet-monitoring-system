from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from apps.core.views import HomePageView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^amf/', 'apps.core.amfgateway.services', name = 'amf_services'),
    url(r'^stream/', include('apps.core.urls', namespace='core')),
    url(r'^$', HomePageView.as_view(), name = 'core:homepageview'),
)

#urlpatterns += patterns('apps.core.views',
#    
#)
