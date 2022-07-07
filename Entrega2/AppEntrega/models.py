from django.db import models

class Familiares (models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    celular=models.IntegerField()
    email= models.EmailField()
    profesion= models.CharField(max_length=30)


class Amigos (models.Model):
    nombre= models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
  