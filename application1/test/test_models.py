from django.test import TestCase   #TestCase pertenece a Unittest  , tambien existe doctest
from application1.models import *
import doctest
from django.contrib.auth.models import User


#      Método 1, base de datos de test
class CategoriaTest(TestCase):

    def test_num_categories(self):
        r = self.assertEqual(0, len(Categoria.objects.all()))
        if not r:
            print("Hay categorías en los datos")
        else:
            print("No hay categorías en los datos")


#      Método 2, con fixtures
class CategoriaTestFixtures(TestCase):

    fixtures = ['dump2.json']

    def test_num_categories(self):
        self.assertEqual(2, len(Categoria.objects.all()) )


class UserTest(TestCase):

    def test_user(self):
        resp = self.client.login(username='elk1oppp')
        if not resp:
            print("No existe el usuario")
        else:
            print("Existe el usuario indicado")
        # resp = self.client.get('/account/vista1/')
        # self.assertEqual(200, resp.status_code)


class DocTest(TestCase):

    def testDoc(self):
        print(doctest.testmod())
        self.assertEqual(2+2,4)
