from django.db import models
from django.contrib.auth.models import User

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


class User_base(models.Model):
	Nom = models.CharField(max_length=40, name='Nombre')
	Ape = models.CharField(max_length=40, name='Apellidos')
	Num_id = models.CharField(max_length=10, unique=True, name='Identificacion')
	Ciu = models.CharField(max_length=60, blank=True, name='Ciudad')
	Dir = models.CharField(max_length=200, blank=True, name='Direccion')
	Tel = models.CharField(max_length=10, blank=True, name='Telefono')
	GEN = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'))
	Sex = models.CharField(max_length=12, choices=GEN, name='Sexo')
	Email = models.EmailField(unique=True, blank=True, name='E-mail')
	Pic = models.ImageField(name='Foto')

	def __str__(self):
		return self.Nom

	class Meta:
		abstract = True


class Administrador(User_base):
	tip_adm = (('Super', 'Super'), ('Admin', 'Admin'))
	Tip_usu = models.CharField(max_length=12, choices=tip_adm, name='Tipo')
	tip_id = (('cc', 'cc'),('ti','ti'),('otro', 'otro'))
	Tip_id = models.CharField(max_length=12, choices=tip_id, name='Tipo de indentificacion')
	Pass = models.CharField(max_length=16, name='Contraseña')
	Usuario = models.ForeignKey(User)
	# Privilegios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class Usuario(User_base):
	EST = (('activo', 'activo'), ('inactivo', 'inactivo'))
	Est = models.CharField(max_length=12, choices=EST, name='Estado')
	Fec_ing = models.DateField(auto_now_add=True, name='Fecha de ingreso')
	Reg_civ = models.ImageField(name='Registro civil')
