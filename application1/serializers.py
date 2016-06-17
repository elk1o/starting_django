from rest_framework import serializers
from application1.models import Espectaculo

class EspectaculoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Espectaculo
        field = ('id', 'espectaculo', 'fecha', 'hora', 'descripcion', 'recaudacion', 'vendidas', 'imagen', 'aforo_completo')