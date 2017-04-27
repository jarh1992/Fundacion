from django.db import models
#from django.contrib.auth.models import User

class Usuario(models.Model):

    tipo = (('empresa', 'empresa'), ('cliente', 'cliente'))
    Tp = models.CharField(max_length=12, choices=tipo)
    Nombre = models.CharField(max_length=40)
    Apellidos = models.CharField(max_length=40, blank=True)
    Identificacion = models.CharField(max_length=10, unique=True)
    estado = (('activo', 'activo'), ('inactivo', 'inactivo'))
    Est = models.CharField(max_length=12, choices=estado)
    Ciudad = models.CharField(max_length=60, blank=True)
    Direccion = models.CharField(max_length=200, blank=True)
    GENERO = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro'))
    Sexo = models.CharField(max_length=12, choices=GENERO, blank=True)
    Fecha_ingreso = models.DateField(auto_now_add=True)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    #usuario = models.OneToOneField(User, related_name="profile")

    def __unicode__(self):
        return self.Nombre