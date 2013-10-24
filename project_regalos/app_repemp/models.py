from django.db import models


class Jurisdiccion(models.Model):
	"""
	Cada centro de responsabilidad pertenece a una determinada jurisdiccion. Asi,
	1 => J1...7 => OC
	"""
	id_jurisdiccion	= models.IntegerField(primary_key=True)
	descr			= models.CharField(max_length=2)

	class Meta:
		db_table	= 'jurisdiccion'

class Adcripcion(models.Model):
	"""
	Plantilla de centros de adscripcion, indicando el cr, la adscripcion fisica
	y la jurisdiccion a la que pertenece. Incluye 0?jubilado
	"""
	id_cr			= models.IntegerField(primary_key=True)
	descr			= models.CharField(max_length=200)
	fisicamente		= models.IntegerField()
	fdescr			= models.CharField(max_length=200)
	jnum			= models.ForeignKey(Jurisdiccion)

	class Meta:
		db_table = 'adscripcion'


class Plantilla(models.Model):
	"""
	Plantilla de personal con posibilidades de ser evaluado. No se asegura nada
	aun pero se excluyen ciertas caracteristicas
	"""
	rfc				= models.CharField(max_length=13, primary_key=True)
	nombre			= models.CharField(max_length=100, null=False)
	cr				= models.ForeignKey(Adscripcion)
	observaciones 	= models.CharField(max_length=200)
	tipo_trabajador = models.CharField(25)

	class Meta:
		db_table = 'plantilla'
