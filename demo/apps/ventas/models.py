from django.db import models

class cliente(models.Model):
	nombre	=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=200)
	status	=models.BooleanField(default=True)
	
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
		return nombreCompleto
	
class producto(models.Model):

	def url(self,filename):
		ruta = "MultimediaData/Producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre	=models.CharField(max_length=200)
	descripcion=models.TextField(max_length=300)
	status	=models.BooleanField(default=True)
	imagen	= models.ImageField(upload_to=url,null=True,blank=True)
	precio	= models.DecimalField(max_digits=6,decimal_places=2)
	stock	= models.IntegerField()
	
	def __unicode__(self):
		return self.nombre
