#from django.db import models

#class LecturaSensor(models.Model):
 #   sensor_id = models.CharField(max_length=50)
   # raw = models.IntegerField()
    #voltage = models.FloatField()
 #   ppmCO2 = models.FloatField()
  #  timestamp = models.DateTimeField(auto_now_add=True)



from django.db import models

class LecturaSensor(models.Model):
    sensor_id = models.CharField(max_length=100)
    raw = models.IntegerField()
    voltage = models.FloatField()
    ppmCO2 = models.FloatField()
    eCO2 = models.FloatField(default=0.0)       # Agregado con default
    TVOC = models.FloatField(default=0.0)       # Agregado con default
    humidity = models.FloatField(default=0.0)   # Agregado con default
    temperature = models.FloatField(default=0.0)  # Agregado con default
    timestamp = models.DateTimeField(auto_now_add=True)