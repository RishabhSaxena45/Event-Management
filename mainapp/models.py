from django.db import models

# Create your models here.
class myreg(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    
    def __str__(self):
        return self.username