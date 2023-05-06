from django.shortcuts import render
from .models import Productions
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
# def PersonaggiView(request):

#     obj = Personaggi.objects.all()
#     context = {}
#     context['attore'] = obj[0].attore
#     return render(request,'personaggi/index.html',  context=context)

class ProductionsView(TemplateView):
    template_name = 'personaggi/index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # context['attore'] = Personaggi.objects.all()[1].attore
        return context

class ProductionsDetail(DetailView):
    model = Productions
    template_name = "productions/productions_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Productions.objects.all()[0:] 
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
        # context['prot'] = Productions.objects.all()[0].protagonisti
        # context['nome'] = Personaggi.objects.all()[0:].nome
        # context['sopranome'] = Personaggi.objects.all()[0:].sopranome
        # context['attore'] = Personaggi.objects.all()[0:].attore
        # context['descrizione'] = Personaggi.objects.all()[0:].descrizione
        # context['ablita'] = Personaggi.objects.all()[0:].abilita
        return context
