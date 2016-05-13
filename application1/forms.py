# -*- coding: utf-8 -*-
from django import forms   # se rescribio el newforms


class Formulario1(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)
    telefono = forms.CharField()


# class Formulario1(forms.Form):
#     asunto = forms.CharField()
#     email = forms.EmailField(required=False)
#     mensaje = forms.Textarea()
