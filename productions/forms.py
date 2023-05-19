from django import forms

class FilterForm(forms.Form):
    Fase_1 = forms.BooleanField(required=False)
    Fase_2 = forms.BooleanField(required=False)
    Fase_3 = forms.BooleanField(required=False)