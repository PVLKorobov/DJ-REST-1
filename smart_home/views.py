from django.shortcuts import render

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView(RetrieveAPIView):
    def get(self, request, id):
        sensorObject = Sensor.objects.filter(id=id)
        if sensorObject.exists():
            sensor = sensorObject.first()
            measurements = sensor.measures.all()
            data = SensorSerializer(sensor).data
            data['measurements'] = MeasurementSerializer(measurements, many=True).data
            return Response(data)
        else:
            return Response({'status':'object does not exist'})

    def post(self, request, name, desc):
        Sensor(name=name, desc=desc).save()
        return Response({'status':'OK'})
    
    def patch(self, request, id, name, desc):
        sensorObject = Sensor.objects.filter(id=id)
        if sensorObject.exists():
            sensorObject.update(name=name, desc=desc)
            return Response({'status':'OK'})
        else:
            return Response({'status':'object does not exist'})

    def delete(self, request, id):
        sensorObject = Sensor.objects.filter(id=id)
        if sensorObject.exists():
            sensor = sensorObject.first()
            sensor.delete()
            return Response({'status':'OK'})
        else:
            return Response({'status':'object does not exist'})
        

@api_view(['POST'])
def fill(request):
    try:
        Sensor.objects.all().delete()
        for i in range(1, 11):
            sensorObj = Sensor(id=i, name='name#'+str(i), desc='description#'+str(i))
            sensorObj.save()
            for j in range(1, 4):
                Measurement(value=3.14*j + i*0.15, sensor=sensorObj).save()
        return Response({'status':'OK'})
    except:
        return Response({'status': "can't add objects"})