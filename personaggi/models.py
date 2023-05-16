from django.db import models
from django.urls import reverse
# Create your models here.
class Personaggi(models.Model):
    nome = models.TextField(max_length=100)
    sopranome = models.TextField(max_length=100)
    slug = models.SlugField(max_length=100 , null=True,unique=True)
    attore = models.TextField(max_length=100,null=True)
    img = models.ImageField(upload_to="image/personaggi/" , null=True, blank=True, default="image/notfound.jpg") 
    descrizione = models.TextField(max_length=10000,null=True)
    abilita = models.TextField(max_length=10000, null=True)


    def __str__(self):
            
        return self.nome
    def get_absolute_url(self):
        return reverse("personaggi:PersonaggiDetail", kwargs={"slug": self.slug})
    
    class Meta():
        verbose_name_plural = "Personaggi"
    