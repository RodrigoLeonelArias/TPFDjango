
# Create your models here.
from django.db import models

# Create your models here.
class Preventista(models.Model):
    """Model definition for Preventista."""

    identificador = models.IntegerField(primary_key=True)
    nombre = models.CharField("Nombre del proveedor", max_length=50)
    domicilio=models.CharField("Domicilio del proveedor", max_length=50)
    ciudad=models.CharField("Ciudad del proveedor", max_length=50)
    rubro = models.CharField("Rubro del proveedor", max_length=50)
    


    class Meta:
        """Meta definition for Preventista."""

        verbose_name = 'Preventista'
        verbose_name_plural = 'Preventistas'

    def __str__(self):
        """Unicode representation of Preventistas."""
        return f"{self.identificador}, {self.nombre}, {self.rubro}"