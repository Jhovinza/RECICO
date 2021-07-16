from django import forms
from .models import *
from django.forms.widgets import DateInput


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rec', 'id_cliente', 'nombre', 'rut', 'direccion', 'telefono', 'correo', 'plan_reciclaje', 'ciudad', 'fecha_entrega']
        widgets = {'fecha_entrega': DateInput(attrs={'type': 'date'})}

    class Media:
        js = ('/admin/jsi18n', '/admin/js/core.js',)


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan_reciclaje
        fields = ['id_plan', 'nombre_plan', 'valor_plan', 'num_retiros']