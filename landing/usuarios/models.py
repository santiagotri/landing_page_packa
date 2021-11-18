from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH, CharField

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=True, default=None, blank=True)
    email = models.EmailField(max_length=100, null=True, default=None, blank=True)
    
    def __str__(self):
        return '{}'.format(self.nombre + " - "+self.email)    