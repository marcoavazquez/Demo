from django.contrib import admin
from demo.apps.ventas.models import cliente,producto

#Registrar los modelos de ventas
admin.site.register(cliente)
admin.site.register(producto)