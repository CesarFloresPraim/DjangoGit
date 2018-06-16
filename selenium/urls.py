from django.conf.urls import  url
from . import views
app_name = 'FirstDjangoApp'
urlpatterns = [
    url(r'^usuarios$', views.Usuarios.as_view(), name="Usuarios"),
    url(r'^istore$', views.Istore.as_view(), name="Istore"),
    url(r'^buscar$', views.buscar, name="buscar"),
    url(r'^buscar_articulos$', views.buscar_articulos, name="buscar_articulos"),
    url(r'^registrar_venta$', views.registrar_venta, name="registrar_venta"),
    url(r'^datos_graficas$', views.get_chart_data, name="datos_graficas"),
    url(r'^registrar$', views.Registrar.as_view(), name="Registrar"),
]
