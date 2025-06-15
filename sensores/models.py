from django.db import models

class LecturaSensor(models.Model):
    sensor_id = models.CharField(max_length=50)
    raw = models.IntegerField()
    voltage = models.FloatField()
    ppmCO2 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
