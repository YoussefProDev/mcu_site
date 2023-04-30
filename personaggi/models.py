from django.db import models

# Create your models here.
class Personaggi(models.Model):
    nome = models.TextField(max_length=50)
    sopranome = models.TextField(max_length=50)
    attore = models.TextField(max_length=50,null=True)