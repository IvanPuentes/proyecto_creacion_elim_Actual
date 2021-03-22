from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text


class Manga(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
   
    def __str__(self):
        return self.text

class DescripLib(models.Model):
    text = models.TextField(default="")
    descrpicion = models.TextField(default="")
    img = models.TextField(default="")
    presio = models.TextField(default="")
   
    def __str__(self):
        return self.text

class Autores(models.Model):
    Nombre = models.TextField(default="")
    Descripcion = models.TextField(default="")
    img = models.TextField(default="")
    Nacionalidad = models.TextField(default="")
    F_Muerte = models.TextField(default="")


    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('descAutores', args=[str(self.id)])