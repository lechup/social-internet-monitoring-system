# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView, TemplateResponseMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect

from apps.core.models import Stream, Category


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
        if 'modal' in self.request.GET:
            context['modal'] = self.request.GET['modal']
        else:
            context['modal'] = None

        return context


class StreamReceiveViewBase(DetailView):
    model = Stream


class StreamReceivePublicView(StreamReceiveViewBase):
    template_name = 'core/stream_detail_receive_public.html'


class StreamReceivePrivateView(StreamReceiveViewBase):   
    template_name = 'core/stream_detail_receive_private.html'

    def dispatch(self, request, *args, **kwargs):
        superclass_return = super(StreamReceivePrivateView, self).dispatch(request, *args, **kwargs)
        if not self.object.is_public:
            return redirect('core-stream_is_private')
        else:
            return superclass_return


class StreamListView(ListView):
    paginate_by = 5
    queryset = Stream.objects.select_related().filter(is_public = True)
    context_object_name = "stream_list"

    def get_queryset(self):
        if len(self.args) > 0:
            return Stream.objects.select_related().filter(categories__slug = self.args[0])
        else:
            return self.queryset

    def get_context_data(self, **kwargs):
        context = super(StreamListView, self).get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        if len(self.args) > 0:
            try:
                context['selected_category'] = Category.objects.select_related().get(slug = self.args[0])
            except ObjectDoesNotExist:
                raise Http404
        else:
            context['selected_category'] = None

        return context


class TemplateContentTypeResponseMixin(TemplateResponseMixin):
    def render_to_response(self, context, **response_kwargs):
        if hasattr(self, 'content_type'):
            response_kwargs['content_type'] = self.content_type 
        elif 'content_type' in self.kwargs:
            response_kwargs['content_type'] = self.kwargs['content_type']

        return super(TemplateContentTypeResponseMixin, self).render_to_response(
            context,
            **response_kwargs
        )


class TemplateContentTypeView(TemplateView, TemplateContentTypeResponseMixin):
    pass


class GeoIPjsView(TemplateContentTypeView):
    template_name = "js/geoip.js"
    content_type = 'text/javascript'

    def get_context_data(self, **kwargs):
        context = super(GeoIPjsView, self).get_context_data(**kwargs)

        from django.contrib.gis.geoip import GeoIP
        context['object'] = GeoIP(path='lib/geoip/')
        context['object'] = context['object'].city(self.request.META['REMOTE_ADDR'])

        return context