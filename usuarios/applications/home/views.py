from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import datetime


class PaginaPrincipalView(TemplateView):
    template_name = 'home/index.html'


# creando mi mixin
class FechaMixin(object):

    def get_context_data(self, **kwargs):
        context = super(FechaMixin, self).get_context_data(**kwargs)
        context['fecha'] = datetime.now()
        return context


class PruebaMixin(FechaMixin, TemplateView):
    template_name = 'home/prueba_mixin.html'
