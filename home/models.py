from django.db import models
# from django.conf import settings
from personaggi.models import Personaggi

# Create your models here.

class Home(models.Model):
    # nome = models.TextField(max_length=50)
    # sopranome = models.TextField(max_length=50)
    personaggi = models.ForeignKey(Personaggi,on_delete= models.CASCADE, null=True)
    