from django.db import models

# Create your models here.

class VendorReg(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)
    def __str__(self):
        return self.username
    
class VendorItem(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    desc = models.TextField(max_length=200)

    
    def __str__(self):
        return self.name