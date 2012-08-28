from django.conf.urls.defaults import patterns, url
from apps.core.views import ReceivingView, ReceivingPrivateView, InfoPrivateStreamView

urlpatterns = patterns('',
    url(r'^is_private/$', InfoPrivateStreamView.as_view(), name = 'privatestreaminfoview'),    
    url(r'^receiving/(?P<slug>[\-\w]+)/$', ReceivingView.as_view(), name = 'receivingview'),
    url(r'^receiving/(?P<slug>[\-\w]+)/(?P<uuid>[_\-\w]+)/$', ReceivingPrivateView.as_view(), name = 'receivingprivateview'),
)
