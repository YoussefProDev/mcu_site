from django.shortcuts import render
from django.views.generic.base import TemplateView
from productions.models import Productions
# from django.db.models import Avg?

# Create your views here.
# def HomeView(request):
#     return render(request,'home/index.html')

class HomeView(TemplateView):
    template_name = "home/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produzioni'] = Productions.objects.all()[0:]
        # context['fasi'] = Productions.objects.all().filter(fase = "fase")
        
        context['f1'] = Productions.objects.all().filter(fase = "Fase 1")
        context['f2'] = Productions.objects.all().filter(fase = "Fase 2")
        context['f3'] = Productions.objects.all().filter(fase = "Fase 3")
        context['f4'] = Productions.objects.all().filter(fase = "Fase 4")
        context['fasi'] = [context['f1'],context['f2'],context['f3'],context['f4']]
        # print(context['fasi'])
        # print("fffff",context['fasi'])
        # context["nfasi"] = len("fasi")2
        # print("nfasi")
        return context

