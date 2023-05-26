from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Productions
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import FilterForm
from django.db.models import Q


class ProductionsDetail(DetailView):
    model = Productions
    template_name = "productions/productions_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Productions.objects.all()[0] 
        print(context['films'].protagonisti)
        # context['nome'] = Personaggi.objects.all()[0].nome
        # context['sopranome'] = Personaggi.objects.all()[0].sopranome
        # context['attore'] = Personaggi.objects.all()[0].attore
        # context['descrizione'] = Personaggi.objects.all()[0].descrizione
        # context['ablita'] = Personaggi.objects.all()[0].abilita
        return context
        
class ProductionsList(ListView):
    model = Productions
    template_name = "productions/productions_list.html"
    # paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Productions.objects.all()[0:] 
        form = FilterForm(self.request.GET)
        
        context['form'] = form
        if form.is_valid():
            filters = Q()
            if form.cleaned_data['Fase_1']:
                # filters['fase'] = "Fase 1"
                filters |= Q(fase="Fase 1")
            if form.cleaned_data['Fase_2']:
                # filters['fase'] = "Fase 2"
                filters |= Q(fase="Fase 2")
            if form.cleaned_data['Fase_3']:
                # filters['fase'] = "Fase 3"
                filters |= Q(fase="Fase 3")
            if filters:
                # print("gggg",filters)
                queryset = Productions.objects.all().filter(filters)
                # for filter_item in filters[1:]:
                #     queryset |= Productions.objects.all().filter(**filter_item)
                context['films'] = queryset

        return context


