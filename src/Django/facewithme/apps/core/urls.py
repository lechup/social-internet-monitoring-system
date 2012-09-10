from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

from apps.core.views import ReceivingView, ReceivingPrivateView, StreamListView

urlpatterns = patterns('',
    url(r'^is_private/$', TemplateView.as_view(template_name = 'core/is_private,html'), name = 'core-stream_is_private'),
    url(r'^list/$', StreamListView.as_view(), name = 'core-stream_list'),
    url(r'^list/([\-\w]+)/$', StreamListView.as_view(), name = 'core-stream_list_category'),
    url(r'^receiving/(?P<slug>[\-\w]+)/$', ReceivingView.as_view(), name = 'core-stream_receiving'),
    url(r'^receiving/(?P<slug>[\-\w]+)/(?P<uuid>[_\-\w]+)/$', ReceivingPrivateView.as_view(), name = 'core-stream_receiving_private'),
)