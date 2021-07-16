import recurrence.fields
from django.db import models


class Plan_reciclaje(models.Model):
    id_plan = models.BigAutoField(primary_key=True)
    nombre_plan = models.CharField(max_length=30, null=False, blank=False)
    valor_plan = models.IntegerField(null=False, blank=False)
    num_retiros = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return(self.nombre_plan)


class Cliente(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False, blank=False)
    rut = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=100, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    correo = models.CharField(max_length=50, null=True, blank=True)
    plan_reciclaje = models.ForeignKey(Plan_reciclaje, null=True, on_delete=models.SET_NULL)
    opCiudad = [("1", "La Serena"), ("2", "Coquimbo")]
    ciudad = models.CharField(max_length=20, blank=False, null=True, choices=opCiudad)
    fecha_entrega = models.DateField(null=True)
    rec = recurrence.fields.RecurrenceField(null=True)

    def __str__(self):
        return(self.nombre)
