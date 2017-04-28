from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver


'''
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
'''


class Fundacion(models.Model):
    Nom = models.CharField(max_length=40)
    Num_id = models.CharField(max_length=10, unique=True)
    Logo = models.ImageField()

    def __str__(self):
        return self.Nom


class Administrador(models.Model):
    tip_adm = (('Super', 'Super'), ('Admin', 'Admin'))
    Tip_usu = models.CharField(max_length=12, choices=tip_adm, name='Tipo')
    Nom = models.CharField(max_length=40, name='Nombre')
    Ape = models.CharField(max_length=40, name='Apellidos')
    tip_id = (('cc', 'cc'),('ti','ti'),('otro', 'otro'))
    Tip_id = models.CharField(max_length=12, choices=tip_id, name='Tipo de indentificacion')
    Num_id = models.CharField(max_length=10, unique=True, name='Identificacion')
    Ciu = models.CharField(max_length=60, blank=True, name='Ciudad')
    Tel = models.CharField(max_length=10, name='Telefono')
    GEN = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro'))
    Sex = models.CharField(max_length=12, choices=GEN, name='Sexo')
    Dir = models.CharField(max_length=25, name='Direccion')
    Email = models.EmailField(unique=True, name='E-mail')
    Pass = models.CharField(max_length=16, name='Contraseña')
    Foto = models.ImageField(name='Foto')
    Usuario = models.ForeignKey(User)
    # Privilegios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __str__(self):
        return self.Nom


class Usuario(models.Model):
    Nom = models.CharField(max_length=40, name='Nombre')
    Ape = models.CharField(max_length=40, blank=True, name='Apellido')
    Num_id = models.CharField(max_length=10, unique=True, name='Identificacion')
    EST = (('activo', 'activo'), ('inactivo', 'inactivo'))
    Est = models.CharField(max_length=12, choices=EST, name='Estado')
    Ciu = models.CharField(max_length=60, blank=True, name='Ciudad')
    Dir = models.CharField(max_length=200, blank=True, name='Direccion')
    GEN = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'))
    Sex = models.CharField(max_length=12, choices=GEN, blank=True, name='Sexo')
    Fec_ing = models.DateField(auto_now_add=True, name='Fecha de ingreso')
    Tel = models.CharField(max_length=10, name='Telefono')
    Email = models.EmailField(unique=True, name='E-mail')
    Foto = models.ImageField()

    def __str__(self):
        return self.Nom