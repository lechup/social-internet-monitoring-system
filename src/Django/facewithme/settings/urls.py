from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from apps.core.views import HomePageView, GeoIPjsView, TemplateContentTypeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^amf/', 'apps.core.amfgateway.services', name = 'core-amfservices'),
    url(r'^stream/', include('apps.core.urls')),
    url(r'^about/$', TemplateView.as_view(template_name = 'about.html'), name = 'core-about'),
    url(r'^crossdomain.xml$', TemplateContentTypeView.as_view(template_name = 'crossdomain.xml'), {'content_type' : 'text/xml'}, name = 'core-about'),
    url(r'^robots.txt$', TemplateContentTypeView.as_view(template_name = 'robots.txt'), {'content_type' : 'text/plain'}, name = 'core-about'),
    url(r'^geoip.js$', GeoIPjsView.as_view(), name = 'core-geoip_js'),
    url(r'^$', HomePageView.as_view(), name = 'core-homepageview'),
)

#urlpatterns += patterns('apps.core.views',
#    
#)
