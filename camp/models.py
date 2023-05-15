from django.db import models
from users.models import Organization
from django.core.validators import MaxValueValidator

# Create your models here.


class Camp(models.Model):
    title = models.CharField(max_length=40)
    orgn = models.ForeignKey(Organization,on_delete=models.DO_NOTHING)
    start = models.DateTimeField()
    end = models.DateTimeField()
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    image = models.ImageField(upload_to='camp/',null=True,blank=True)
    donations = models.IntegerField(default=0)
    receivings = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Donations(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    image = models.ImageField(upload_to='camp/resources/',null=True,blank=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Receivings(models.Model):
    item = models.OneToOneField(Donations,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10,null=True,blank=True)

class Donor(models.Model):
    in_camp = models.BooleanField(default=False)    # Else Individually
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

class Receiver(models.Model):
    in_camp = models.BooleanField(default=False)    # Else Individually
    address = models.CharField(max_length=100)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)