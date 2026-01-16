from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    count = models.IntegerField()
    
    def __str__(self): 
        return self.name