from django.db import models


class PersonasDatos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(default=10)

    def __str__(self):
        return '%s, %s' % (self.nombre, self.apellido)

    class Meta:
        db_table = 'datos'
