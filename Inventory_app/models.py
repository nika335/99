from django.db import models

class Trackin(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    value = models.FloatField()
    def __str__(self):
        return self.name
