from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProducto
from demo.apps.ventas.models import producto 
from django.http import HttpResponseRedirect

def add_producto_view(request):
	info = "Inicializando"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProducto(request.POST,request.FILES)
			if form.is_valid():
				nombre = form.cleaned_data['nombre']
				descripcion = form.cleaned_data['descripcion']
				imagen = form.cleaned_data['imagen']
				precio = form.cleaned_data['precio']
				stock = form.cleaned_data['stock']
				p = producto()
				if imagen:
					p.imagen = imagen
				p.nombre = nombre
				p.descripcion = descripcion
				p.precio = precio
				p.stock = stock
				p.status = True
				p.save() # guradar la informacion
				info = "Se guardo satisfactoriamente"
			else:
				info = "Informacion con datos incorrectos"
			
		form = addProducto()
		ctx = {'form':form,'informacion':info}
		return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
	
	else:
		return HttpResponseRedirect('/')
# Create your views here.
