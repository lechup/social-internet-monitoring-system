from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect

from apps.core.models import Entry

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['whatever'] = (1,2,3)

        return context


class InfoPrivateStreamView(TemplateView):
    template_name = 'info/private_stream.html'


class ReceivingView(DetailView):
    model = Entry
    template_name = 'entry/receiving_detail.html'

    def dispatch(self, request, *args, **kwargs):
        superclass_return = super(ReceivingView, self).dispatch(request, *args, **kwargs)
        if not self.object.is_public:
            return redirect('core:privatestreaminfoview')
        else:
            return superclass_return


class ReceivingPrivateView(DetailView):
    model = Entry
    template_name = "entry/receiving_detail.html"
    
    def dispatch(self, request, *args, **kwargs):
        superclass_return = super(ReceivingPrivateView, self).dispatch(request, *args, **kwargs)
        print self.uuid
        if self.object.uuid == self.uuid:
            return redirect('core:privatestreaminfoview')
        else:
            return superclass_return
