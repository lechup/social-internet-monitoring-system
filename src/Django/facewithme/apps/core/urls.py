from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

from apps.core.views import StreamReceivePrivateView, StreamReceivePublicView, StreamListView

urlpatterns = patterns('',
    url(r'^is_private/$', TemplateView.as_view(template_name = 'stream/is_private,html'), name = 'core-stream_is_private'),
    url(r'^list/$', StreamListView.as_view(), name = 'core-stream_list'),
    url(r'^list/([\-\w]+)/$', StreamListView.as_view(), name = 'core-stream_list_category'),
    url(r'^receive/(?P<slug>[\-\w]+)/$', StreamReceivePublicView.as_view(), name = 'core-stream_item_receive_public'),
    url(r'^receive/(?P<slug>[\-\w]+)/(?P<uuid>[_\-\w]+)/$', StreamReceivePrivateView.as_view(), name = 'core-stream_item_receive_private'),
)