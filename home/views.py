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
        context['f1'] = Productions.objects.all().filter(fase = "F1")
        context['f2'] = Productions.objects.all().filter(fase = "F2")
        context['f3'] = Productions.objects.all().filter(fase = "F3")
        context['f4'] = Productions.objects.all().values('fase').filter(fase = "F4")
        # print(context['fasi'])
        # print("fffff",context['fasi'])
        # context["nfasi"] = len("fasi")2
        # print("nfasi")
        return context

