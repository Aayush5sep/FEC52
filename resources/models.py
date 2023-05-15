from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    image = models.ImageField(upload_to='resources/',null=True,blank=True)
    classno = models.IntegerField(validators=[MaxValueValidator(16)])
    orgn = models.BooleanField(default=False)
    helperid = models.UUIDField()
    address = models.CharField(max_length=100)
    donated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Clothes(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    image = models.ImageField(upload_to='resources/',null=True,blank=True)
    orgn = models.BooleanField(default=False)
    helperid = models.UUIDField()
    address = models.CharField(max_length=100)
    donated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Miscellaneous(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(10)])
    image = models.ImageField(upload_to='resources/',null=True,blank=True)
    orgn = models.BooleanField(default=False)
    helperid = models.UUIDField()
    address = models.CharField(max_length=100)
    donated = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class BookReq(models.Model):
    book = models.ForeignKey(Book,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    whyneed = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title + " " + self.name

class ClothesReq(models.Model):
    clothes = models.ForeignKey(Clothes,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    whyneed = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.clothes.title + " " + self.name

class MiscReq(models.Model):
    item = models.ForeignKey(Miscellaneous,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    whyneed = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    accepted = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.item.title + " " + self.name