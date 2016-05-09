#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
from django.db import models
from django.contrib.auth.models import User

#ORM no tienes que utilizar sentencias sql  clase POCO/POJO

class Categoria(TestCase):
    categoria= models.CharField(max_length=25)
    borrado= models.CharField(max_length=1)

    def __unicode__(self):
        return self.categoria

class Lugar(TestCase):
    lugar = models.CharField(max_length=25)
    borrado = models.CharField(max_length=1)

    def __unicode__(self):
        return u'%s %s' % (self.categoria, self.borrado)

class Espectaculo(TestCase):
    espectaculo = models.CharField(max_length=30)
    fecha = models.DateField()
    hora = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    recaudacion = models.DecimalField(decimal_places=2, max_digits=10)
    vendidas = models.IntegerField()
    imagen = models.CharField(max_length=255)
    aforo_completo = models.BooleanField()
    '''Foreign keys '''
    #categoria = models.ForeignKey(Categoria)
    #lugar = models.ForeignKey(Lugar)
    ''' .BigIntegerField(), CommaSeparatedIntegerField(), EmailField(), FileField(),
     FilePathField(), FloatField(), ImageField() -> BLOB binary, IPAdressField(),
     GenericIPAdressField(), ManyToManyField(), NullBooleanField(), PhoneNumberField(), PositiveIntegerField(), TextField()
     tipos int    tiny o byte  small medium  large huge mongous    IntegerField, PositiveSmallIntegerField PositiveIntegerField(), SlugField()
     '''




