from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Individual(models.Model):
    uid = models.UUIDField(primary_key=True,default = uuid.uuid5)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    age = models.IntegerField(null=True,blank=True)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    longitude = models.CharField(verbose_name="Longitude",max_length=50)
    latitude = models.CharField(verbose_name="Latitude",max_length=50)
    donations = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'
    
class Organization(models.Model):
    uid = models.UUIDField(primary_key=True,default = uuid.uuid5)
    orgn = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True,blank=True)
    contact = models.CharField(max_length=10)
    alt_contact = models.CharField(max_length=10,null=True,blank=True)
    address = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=8)
    country = models.CharField(max_length=50)
    longitude = models.CharField(verbose_name="Longitude",max_length=50)
    latitude = models.CharField(verbose_name="Latitude",max_length=50)
    verified = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    donations = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.orgn}'