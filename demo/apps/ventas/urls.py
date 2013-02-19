from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.ventas.views',
	url(r'^add/productos/$','add_producto_view',name="vista_agregar_producto"),
)