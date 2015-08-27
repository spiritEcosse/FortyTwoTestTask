__author__ = 'igor'
from django.views.generic.base import TemplateView
from apps.hello.models import Contacts


class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.all()
        return context