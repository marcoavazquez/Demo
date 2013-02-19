from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import producto
from demo.apps.home.forms import ContactoForm,LoginForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect 
from django.core.paginator import Paginator,EmptyPage,InvalidPage

def index_view(request):
	mensaje="Esto es un mensaje desde la vista"
	ctx={'msg':mensaje}
	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def productos_view(request,pagina):
	lista_prod = producto.objects.filter(status=True) #Select * from ventas where status = true
	paginator=Paginator(lista_prod,4) #CUANTOS PRODUCTOS POR PAGINA
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx={'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleProducto_view(request,id_prod):
	prod = producto.objects.get(id=id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/singleProducto.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False # Definir si se envio la informacion
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']

			# Configuracion de correo

			to_admin = 'mrc_ant_18@hotmail.com'
			html_content = "Informacion recibida <br>Mensaje:<br>%s"%(texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #definir conternido como html
			msg.send()

	else:
		formulario = ContactoForm()

	ctx = {'form':formulario,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
						mensaje = "Nombre de usuario o algo esta mal"

		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

# Create your views here.
