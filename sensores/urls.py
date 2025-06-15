from django.urls import path
from .views_NoVisual import recibir_datos_sensor, ver_graficas, datos_co2_json

urlpatterns = [
    path('api/sensores', recibir_datos_sensor),
    path('graficas', ver_graficas),
    path('api/datos-co2/', datos_co2_json, name='datos_co2_json'),

]
