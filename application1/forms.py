# -*- coding: utf-8 -*-
from django import forms   # se rescribio el newforms

# class Formulario1(forms.Form):
#     asunto = forms.CharField()
#     email = forms.EmailField(required=False)
#     mensaje = forms.Textarea()


class Formulario1(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(required=False, label="Tu email")
    mensaje = forms.CharField(widget=forms.Textarea)
    telefono = forms.CharField(max_length=9)

    #reglas de validación propias  con automatismo de django
    #   django busca metodos que comiencen por clean_   y tiene que terminar con el nombre del campo
    def clean_mensaje(self):
        mensaje= self.cleaned_data['mensaje']
        num_palabras= len(mensaje.split())
        if num_palabras < 3:
            raise forms.ValidationError("Es necesario introducir al menos 3 palabras")
        return mensaje

    # clean_telefono o lo que sea



