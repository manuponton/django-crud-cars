from django.db import models
class Vehicle(models.Model):
    eid = models.CharField(max_length=20)
    etypeVehicle = models.CharField(max_length=100)
    emodel = models.CharField(max_length=100)
    ebrand = models.CharField(max_length=100)
    eplate = models.CharField(max_length=100)
    emileage = models.CharField(max_length=100)
    class Meta:
        db_table = "vehicle"