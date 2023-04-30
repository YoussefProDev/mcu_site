from django.db import models

# Create your models here.

class Home(models.Model):
    nome = models.TextField(max_length=50)
    sopranome = models.TextField(max_length=50)
    