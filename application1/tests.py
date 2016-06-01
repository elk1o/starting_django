#-*- coding: utf-8 -*-
from django.test import TestCase

# Create your tests here.
from django.db import models
from .models import Categoria, Lugar, Ticket, User, Espectaculo
from django.contrib.auth.models import User

#ORM no tienes que utilizar sentencias sql  clase POCO/POJO

class CategoriaTest(TestCase):
    def setUp(self):
        self.cate = Categoria.objects.create(
            categoria='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
            borrado=1
        )

    def test_categoria_field_lenght(self):
        print(len(self.cate.categoria))
    pass
class Lugar(TestCase):
    pass
class Espectaculo(TestCase):
    #def setUp(self): #Método para insertar registros en la BD
    pass



