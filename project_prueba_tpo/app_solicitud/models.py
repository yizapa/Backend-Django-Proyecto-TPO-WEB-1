from django.db import models

# Create your models here.
class Solicitud(models.Model):
    """
    Atributos de clase que son usadas por herencia de la clase Model
    """
    
    mensaje = models.CharField(max_length=200)
    prioridad = models.PositiveSmallIntegerField(blank=False, null=False)
    pto = models.FloatField(blank=True, null=True)
    hora = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    actualizado = models.DateTimeField(auto_now = True, blank = True)
    
    
    
    # podemos crear la tabla con un nombre especifico pero se lo tenemos
    # que indicar directamente en la metaclase
    
    class Meta:
      db_table = "solicitud_table"
    
    def __str__(self):
        return f"La solicitud: {self.mensaje}, Prioridad {self.prioridad}, Hora {self.hora}, Actualizada {self.actualizado}"

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]