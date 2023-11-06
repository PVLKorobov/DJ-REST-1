from django.db import models


class Sensor(models.Model):
    name = models.TextField()
    desc = models.TextField(blank=True)

class Measurement(models.Model):
    value = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measures')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)