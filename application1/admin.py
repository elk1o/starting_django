from django.contrib import admin

# Register your models here.

from .models import Categoria
from django.contrib import admin

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['']

