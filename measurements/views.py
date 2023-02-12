from .logic import measurements_logic as me
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = me.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = me.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        measurement_dto = me.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'DELETE':
        measurement_dto = me.delete_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = me.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = me.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    
    if request.method == 'DELETE':
        measurement_dto = me.delete_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    