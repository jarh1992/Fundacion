from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Multimedia(models.Model):
    def image_path(self, filename):
        ruta = "Multimedia/%s" % (str(filename))
        return ruta

    Imagen = models.ImageField(upload_to=image_path)

    def __str__(self):
        return self.Imagen.name


@receiver(pre_delete, sender=Multimedia)
def Multimedia_pre_delete_handler(sender, instance, **kwargs):
    instance.Imagen.delete(False)


class Fundacion(models.Model):
    Nom = models.CharField(max_length=40)
    Id = models.CharField(max_length=10, unique=True)
    Logo = models.ImageField(Multimedia)

    def __str__(self):
        return self.Nom


class Administrador(models.Model):
    tip_adm = (('Super', 'Super'), ('Admin', 'Admin'))
    Tip_usu = models.CharField(max_length=12, choices=tip_adm)
    Nom = models.CharField(max_length=40)
    Ape = models.CharField(max_length=40)
    tip_id = (('cc', 'cc'),('ti','ti'),('otro', 'otro'))
    Tip_id = models.CharField(max_length=12, choices=tip_id)
    num_id = models.CharField(max_length=10, unique=True)
    Ciu = models.CharField(max_length=60, blank=True)
    Tel = models.CharField(max_length=10)
    GEN = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro'))
    Sex = models.CharField(max_length=12, choices=GEN)
    Dir = models.CharField(max_length=25)
    Email = models.EmailField(unique=True)
    Pass = models.CharField(max_length=16)
    Pic = models.ImageField(Multimedia)
    usuario = models.ForeignKey(User)
    # Privilegios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        return self.Nom


class Usuario(models.Model):
    Nombre = models.CharField(max_length=40)
    Apellidos = models.CharField(max_length=40, blank=True)
    Identificacion = models.CharField(max_length=10, unique=True)
    stado = (('activo', 'activo'), ('inactivo', 'inactivo'))
    Estado = models.CharField(max_length=12, choices=stado)
    Ciudad = models.CharField(max_length=60, blank=True)
    Direccion = models.CharField(max_length=200, blank=True)
    ESTADO = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro'))
    Sexo = models.CharField(max_length=12, choices=ESTADO, blank=True)
    Fecha_ingreso = models.DateField(auto_now_add=True)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    usuario = models.OneToOneField(User, related_name="profile")

    def __str__(self):
        return self.Nombre