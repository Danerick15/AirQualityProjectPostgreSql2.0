from django.shortcuts import render 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import LecturaSensor
from .serializers import LecturaSensorSerializer
import json
from django.http import JsonResponse
from django.utils.timezone import now, timedelta, localtime

# POST: Recibe datos desde el sensor
@api_view(['POST'])
def recibir_datos_sensor(request):
    serializer = LecturaSensorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"mensaje": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET: Renderiza la plantilla HTML con las gráficas
def ver_graficas(request):
    lecturas = LecturaSensor.objects.order_by('-timestamp')[:50][::-1]

    labels = [l.timestamp.strftime("%Y-%m-%d %H:%M:%S") for l in lecturas]
    raw_data = [l.raw for l in lecturas]
    voltage_data = [l.voltage for l in lecturas]
    co2_data = [l.ppmCO2 for l in lecturas]

    context = {
        'labels': json.dumps(labels),
        'raw_data': json.dumps(raw_data),
        'voltage_data': json.dumps(voltage_data),
        'co2_data': json.dumps(co2_data),
    }
    return render(request, 'graficas.html', context)

# GET: Devuelve datos CO₂ en formato JSON para la gráfica
def datos_co2_json(request):
    try:
        ahora = now()

        dias_param = request.GET.get('dias')
        resultados_param = request.GET.get('resultados')
        escala_param = request.GET.get('escala')

        # Lógica para determinar el intervalo de tiempo
        if not dias_param and not resultados_param and not escala_param:
            fecha_inicio = ahora - timedelta(minutes=25)  # valor por defecto
        elif escala_param and escala_param != 'diario':
            try:
                escala_min = int(escala_param)
                fecha_inicio = ahora - timedelta(minutes=escala_min)
            except ValueError:
                return JsonResponse({'error': 'Escala inválida'}, status=400)
        elif dias_param:
            fecha_inicio = ahora - timedelta(days=int(dias_param))
        else:
            fecha_inicio = ahora - timedelta(minutes=25)

        lecturas = LecturaSensor.objects.filter(timestamp__gte=fecha_inicio).order_by('-timestamp')

        if resultados_param:
            lecturas = lecturas[:int(resultados_param)]

        lecturas = list(lecturas)[::-1]

        labels = [localtime(l.timestamp).strftime("%H:%M:%S") for l in lecturas]
        co2_data = [l.ppmCO2 for l in lecturas]

        return JsonResponse({'labels': labels, 'co2_data': co2_data})

    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status=500)