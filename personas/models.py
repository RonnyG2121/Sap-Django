from django.db import models

# Create your models here.

class Domicilio(models.Model):
    calle = models.CharField(max_length=30)
    numero = models.IntegerField()
    pais = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"Domicilio {self.id}. {self.calle} {self.numero} {self.pais}"

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f"""
        Persona con el ID {self.id}:

Nombre: {self.nombre}.

Apellido: {self.apellido}.

Teléfono: {self.telefono}."""
