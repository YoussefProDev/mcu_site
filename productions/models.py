from django.db import models
from django.urls import reverse
from personaggi.models import Personaggi
from django import forms
# Create your models here.
class Productions(models.Model):
    nome = models.TextField(max_length=50)
    # sopranome = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50 , null=True)
    # attore = models.TextField(max_length=50,null=True)
    # img = models.ImageField(upload_to="media/image/personaggi/" , null=True, blank=True)
    fasi = [
        ("F1","Fase 1"),
        ("F2","Fase 2"),
        ("F3","Fase 3"),
        ("F4","Fase 4"),
        ("F5","Fase 5"),
    ]
    fase = models.CharField(max_length=2 ,choices=fasi,default=fasi[-1])
    descrizione = models.TextField(max_length=500,null=True)
    uscita = models.DateField(null=True)
    # protagonisti = models.TextField(max_length=100, null=True)
    protagonisti = models.ForeignKey(Personaggi,on_delete= models.CASCADE, null=True)


    def __str__(self):
            
        return self.nome
    def get_absolute_url(self):
        return reverse("personaggi:PersonaggiDetail", kwargs={"slug": self.slug})
    
    class Meta():
        verbose_name_plural = "Productions"
    