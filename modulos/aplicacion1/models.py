from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

class Estudias(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    appaternos = models.CharField(max_length=35)
    apmaternos = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M','Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt= '{0} {1}, {2}'
        return txt.format(self.apmaternos, self.appaternos, self.nombre)
