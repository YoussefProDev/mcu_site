from django.shortcuts import render
from .models import Personaggi
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
# def PersonaggiView(request):

#     obj = Personaggi.objects.all()
#     context = {}
#     context['attore'] = obj[0].attore
#     return render(request,'personaggi/index.html',  context=context)

class PersonaggiView(TemplateView):
    template_name = 'personaggi/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['attore'] = Personaggi.objects.all()[1].attore
        return context

class PersonaggiDetail(DetailView):
    model = Personaggi

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['nome'] = Personaggi.objects.all()[0].nome
        context['sopranome'] = Personaggi.objects.all()[0].sopranome
        context['attore'] = Personaggi.objects.all()[0].attore
        context['descrizione'] = Personaggi.objects.all()[0].descrizione
        context['ablita'] = Personaggi.objects.all()[0].abilita
        return context

class PersonaggiList(ListView):
    model = Personaggi
    # paginate_by = 100  # if pagination is desired
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nome'] = Personaggi.objects.all()[0].nome
        context['sopranome'] = Personaggi.objects.all()[0].sopranome
        context['attore'] = Personaggi.objects.all()[0].attore
        context['descrizione'] = Personaggi.objects.all()[0].descrizione
        context['ablita'] = Personaggi.objects.all()[0].abilita
        return context