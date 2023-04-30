from typing import Any, Dict
from django.shortcuts import render
from .models import Personaggi
from django.views.generic.base import TemplateView
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