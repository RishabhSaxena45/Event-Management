from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class EventModel(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    contact = models.IntegerField()
    event_type = models.CharField(max_length=20)
    guest = models.IntegerField()
    event_date = models.TextField()
    
    def __str__(self):
        return self.name

class Guest(models.Model):
    eventhead = models.CharField(max_length=20)
    guest1 = models.CharField(max_length=20)
    guest1age = models.IntegerField()
    guest1gender = models.CharField(max_length=10)
    guest2 = models.CharField(max_length=20)
    guest2age = models.IntegerField()
    guest2gender = models.CharField(max_length=10)
    guest3 = models.CharField(max_length=20)
    guest3age = models.IntegerField()
    guest3gender = models.CharField(max_length=10)
    guest4 = models.CharField(max_length=20)
    guest4age = models.IntegerField()
    guest4gender = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.eventhead