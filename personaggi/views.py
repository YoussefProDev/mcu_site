from django.shortcuts import render,get_object_or_404
from .models import Personaggi
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from productions.models import Productions



class PersonaggiDetail(DetailView):
    model = Personaggi
    template_name = "personaggi/personaggi_detail.html"
    # context_object_name = 'personaggi'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    # def get_object(self, queryset=None):
    #     # Recupera lo slug dal kwargs dell'URL
    #     slug = self.kwargs.get('slug')

    #     # Filtra il queryset per recuperare solo l'oggetto con lo slug corrispondente
    #     queryset = Productions.objects.filter(slug=slug)

    #     # Richiama il metodo get_object() della classe padre
    #     obj = super().get_object(queryset=queryset)
    #     print("fff", obj)
    #     return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        
        # print( "fff ",Productions.objects.all().filter())
        film = self.get_object()

        # film = get_object_or_404(Productions,slug)
        context['presenti'] = film.RFilms.all()
        # print(context['presenti'])
        # print(context['productions'])
        # context['sopranome'] = Personaggi.objects.all()[0].sopranome
        # context['attore'] = Personaggi.objects.all()[0].attore
        # context['descrizione'] = Personaggi.objects.all()[0].descrizione
        # context['ablita'] = Personaggi.objects.all()[0].abilita
        return context

class PersonaggiList(ListView):
    model = Personaggi
    # paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['personaggi'] = Personaggi.objects.all()[0:] 
        # context['nome'] = Personaggi.objects.all()[0:].nome
        # context['sopranome'] = Personaggi.objects.all()[0:].sopranome
        # context['attore'] = Personaggi.objects.all()[0:].attore
        # context['descrizione'] = Personaggi.objects.all()[0:].descrizione
        # context['ablita'] = Personaggi.objects.all()[0:].abilita
        return context
