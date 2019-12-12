from django.db import models

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField("Nombre:",max_length=45)
    descripcion = models.TextField(max_length=45)
    empresa = models.CharField (max_length=45)
    fecha = models.DateField(null=True)
    imagen =  models.ImageField('Cargar imagen',upload_to='fotos/', default = 'fotos/profile.png', blank=True, null=True)

    def admin_foto(self):
        if self.foto:
            return mark_safe('<img src="{0}" width="80" height="90" alt="foto" style="border-radius: 5px">'.format(self.foto.url)) #135X140 #<a href="{0}"><img src="{0}" width="100" height="110" alt="Sin foto"></a>
        else:
            return mark_safe('<img src="{% static "fotos/profile.png" %}" width="90" height="70" alt="Usuario sin foto" style="border-radius: 5px"/>')


    def __str__(self):
        return self.nombre

class espacios(models.Model):
    nombre = models.CharField("Nombre:", max_length=45)
    casaEventos = models.TextField(max_length=45)
    descripcion = models.TextField(max_length=45)
    precio = models.IntegerField()
    
    def __str__(self):
        return "{0}-{1}".format(self.nombre, self.casaEventos)

class EspacioOtro(models.Model):
    nombre = models.CharField("Nombre:", max_length=45)
    casaEventos = models.TextField(max_length=45)
    descripcion = models.TextField(max_length=45)
    precio = models.IntegerField()
    
    def __str__(self):
        return "{0}-{1}".format(self.nombre, self.casaEventos)


class servicios(models.Model):
    nombre = models.CharField("Nombre:", max_length=45)
    prestador = models.TextField(max_length=45)
    descripcion = models.TextField(max_length=45)
    precio = models.IntegerField()
    
    def __str__(self):
        return "{0}-{1}".format(self.nombre)
    