from django.db import models
from django.urls import reverse
from personaggi.models import Personaggi
from django import forms
# Create your models here.
class Productions(models.Model):
    nome = models.TextField(max_length=100)
    # sopranome = models.TextField(max_length=50)
    slug = models.SlugField(max_length=100 , null=True)
    # attore = models.TextField(max_length=50,null=True)
    img = models.ImageField(upload_to="image/productions/" , null=True, blank=True, default="image/notfound.jpg")
    fasi = [
        ("Fase 1","Fase 1"),
        ("Fase 2","Fase 2"),
        ("Fase 3","Fase 3"),
        ("Fase 4","Fase 4"),
        ("Fase 5","Fase 5"),
    ]
    fase = models.CharField(max_length=10 ,choices=fasi,default=fasi[-1])
    # print(fase)
    print(len(fasi))
    descrizione = models.TextField(max_length=10000,null=True)
    uscita = models.DateField(null=True)
    protagonisti = models.ManyToManyField(Personaggi, related_name="protagonisti")
    # protagonisti = models.ForeignKey(Personaggi,on_delete= models.CASCADE, null=True)
    
    


    def __str__(self):
            
        return self.nome
    def get_absolute_url(self):
        return reverse("productions:ProductionsDetail", kwargs={"slug": self.slug})
    
    class Meta():
        verbose_name_plural = "Productions"
        ordering = ["uscita"]
     