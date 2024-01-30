from django.db import models

# Create your models here.
class account(models.Model):
    accnumber=models.CharField(max_length=1000)
    IFSC=models.CharField(max_length=1000)
    accholder=models.CharField(max_length=1000)

class Bankdetails(models.Model):
    accnumber=models.CharField(max_length=1000)
    IFSC=models.CharField(max_length=1000)
    accholder=models.CharField(max_length=1000)
