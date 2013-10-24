#core

from django.db import models

from app_repemp.models import Plantilla
#from repemp.models import Seccion
#from repemp.models import Relacion


class Relacion(models.Model):
	"""
	La relacion laboral del trabajador con el organismo.
	Los valores pueden ser variables, pero los mas comunes
	son: BASE, REGULARIZADO. Puesto que aun no se contempla
	a personal eventual.
	"""
	id_relacion 	= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=50)

	class Meta:
		db_table = 'relacion'

class Seccion(models.Model):
	"""
	La seccion sindical a la cual pertenece: 
	"""
	seccion			= models.CharField(max_length=25, primary_key=True)
	descr			= models.CharField(max_length=50)

	class Meta:
		db_table = 'seccion'

class Sorteo(models.Model):
	"""
	Personal que sera evaluado (validado) para participar en el sorteo de
	regalos correspondiente.
	"""
	rfc				= models.ForeignKey(Plantilla)
	nombre			= models.CharField(max_length=100)
	cr				= models.IntegerField()
	fisicamente		= models.IntegerField()
	seccion			= models.ForeignKey(Seccion)
	observaciones	= models.CharField(max_length=200)
	tipo_trabajador	= models.ForeignKey(Relacion)

	class Meta:
		db_table = 'sorteo'


class Reporta(models.Model):
	"""
	De que delegacion reporta al personal
	"""
	id_reporta		= models.IntegerField(primary_key=True)
	descr			= models.CharField(max_length=100)

	class Meta:
		db_table = 'seccion'

class Tipo(models.Model):
	"""
	Pieza, Unidad, Paquete, del tipo de regalo
	"""
	id_tipo			= models.CharField(max_length=10, primary_key=True)
	descr			= models.CharField(max_length=25)

	class Meta:
		db_table = 'tipo'

class Tamanio(models.Model):
	"""
	Generalmente se manejan solo dos tipos: GRandes y CHicos
	"""
	id_tamanio		= models.CharField(max_length=10, primary_key=True)
	descr			= models.CharField(max_length=25)

	class Meta:
		db_table = 'tamanio'

class Regalo(models.Model):
	"""
	Descripcion, cantidad y anio de los regalos otorgados por las autoridades
	(jefatura y sindicato), si aplica.
	"""
	id_regalo		= models.CharField(max_length=25, primary_key=True)
	short_descr		= models.CharField(max_length=100)
	long_descr		= models.CharField(max_length=200)
	tipo			= models.ForeignKey(Tipo)
	tamanio			= models.ForeignKey(Tamanio)
	total			= models.IntegerField()
	anio			= models.IntegerField()

	class Meta:
		db_table = 'regalo'
		
class Distribucion(models.Model):
	"""
	Asignacion de ragalos por delegacion. Previo analisis con el anio proximo
	anterior
	"""
	id_distribucion = models.IntegerField(primary_key=True)
	reporta			= models.ForeignKey(Reporta)
	regalo			= models.ForignKey(Regalo)
	anio			= models.IntegerField()
	cantidad		= models.IntegerField()

	class Meta:
		db_table = 'distribucion'
