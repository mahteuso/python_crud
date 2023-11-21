from django.db import models

class Equipament(models.Model):
    equipament_name = models.CharField(max_length=250)
    lab_name = models.CharField(max_length=250)
    patrimony = models.IntegerField()