from django.contrib import admin

# Register your models here.

from .models import Categoria, Lugar, Espectaculo
from django.contrib import admin
from .forms import FormCategoria

# @admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ('id','categoria', 'borrado')
    form = FormCategoria


class LugarAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ('id','lugar', 'borrado')


class EspectaculoAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ('id','espectaculo', 'fecha', 'descripcion')
    list_filter = ('fecha', )
    ordering = ('fecha', )
    date_hierarchy = 'fecha'
    # fields = ('espectaculo','descripcion','id', )
    # filter_horizontal = ('fecha', )

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Lugar, LugarAdmin)
admin.site.register(Espectaculo, EspectaculoAdmin)

# Otra forma de registrar el modelo en admin(sin decorador):
# admin.site.register(Categoria)  # utiliza de forma indirecta la clase AdminSite
