#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

#ORM no tienes que utilizar sentencias sql  clase POCO/POJO

class Categoria(models.Model):

    categoria= models.CharField(
        max_length=25,
    )

    borrado= models.CharField(
        max_length=1,
        default=u'1'
    )

    def __unicode__(self):
        return self.categoria

    def __str__(self):
        return self.categoria

    class Admin:
        list_display = ('categoria','borrado')
        list_filter =  ('categoria')
        ordering =     ('-categoria',)
        search_fields = ('categoria',)
        pass

class Lugar(models.Model):

    lugar = models.CharField(
        max_length=25,
    )

    borrado = models.CharField(
        max_length=1,
    )

    class Meta:
        #Pluralización en el admin
        verbose_name_plural = "Lugares"
        #Ordena los datos por orden ascendente
        ordering = ["-id"]
        pass

    class Admin:
        list_display = ('Id', 'Lugar', 'borrado')
        pass

    def __unicode__(self):
        return u'%s %s' % (self.categoria, self.borrado)

class Espectaculo(models.Model):

    espectaculo = models.CharField(
        max_length=30,
    )

    fecha = models.DateField()

    hora = models.DateTimeField()

    descripcion = models.CharField(
        max_length=255,
    )

    recaudacion = models.DecimalField(
        decimal_places=2,
        max_digits=10,
    )

    vendidas = models.IntegerField()

    imagen = models.CharField(
        max_length=255,
    )

    aforo_completo = models.BooleanField()

    '''Foreign keys '''
    categoria = models.ForeignKey(Categoria)

    lugar = models.ForeignKey(Lugar)
    ''' .BigIntegerField(), CommaSeparatedIntegerField(), EmailField(), FileField(),
     FilePathField(), FloatField(), ImageField() -> BLOB binary, IPAdressField(),
     GenericIPAdressField(), ManyToManyField(), NullBooleanField(), PhoneNumberField(), PositiveIntegerField(), TextField()
     tipos int    tiny o byte  small medium  large huge mongous    IntegerField, PositiveSmallIntegerField PositiveIntegerField(), SlugField()
     '''

class Ticket(models.Model):

    pin = models.CharField(
        max_length=50,
        verbose_name='Pin',
    )

    fecha = models.DateTimeField(
        auto_now_add=True, #Añade automáticamente la fecha en la que es creado el registro
        verbose_name='Fecha',
    )

    # numero = models.AutoField(primary_key=True) No tiene sentido, a no ser que se aplique primary_key=True



