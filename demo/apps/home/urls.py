from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^productos/page/(?P<pagina>.*)/$','productos_view',name='vista_productos'),
	url(r'^producto/(?P<id_prod>.*)/$','singleProducto_view',name='vista_singleProducto'),
	url(r'^contacto/$','contacto_view',name='vista_contacto'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
)