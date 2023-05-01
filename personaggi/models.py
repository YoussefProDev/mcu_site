from django.db import models
from django.urls import reverse
# Create your models here.
class Personaggi(models.Model):
    nome = models.TextField(max_length=50)
    sopranome = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50 , null=True)
    attore = models.TextField(max_length=50,null=True)
    img = models.ImageField(upload_to="media/image/personaggi/" , null=True, blank=True)
    descrizione = models.TextField(max_length=500,null=True)
    abilita = models.TextField(max_length=50, null=True)


    def __str__(self):
            
        return self.nome
    def get_absolute_url(self):
        return reverse("personaggi:PersonaggiDetail", kwargs={"slug": self.slug})
    
    class Meta():
        verbose_name_plural = "Personaggi"
    