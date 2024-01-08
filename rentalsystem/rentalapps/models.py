from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class customusers(AbstractUser):
    Title = models.CharField(max_length=244)
    address = models.CharField(max_length=225, null=True)
    user_type = models.IntegerField(null=True)
    image = models.FileField()
    phone = models.IntegerField(null=True)
    location = models.CharField(max_length=255,null=True)
    company_name = models.CharField(max_length=225,null=True)

    def __str__(self):
        return self.username



class Car(models.Model):
    company_id = models.ForeignKey(customusers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    image = models.FileField()
    car_model = models.CharField(max_length=225,null=True)
    details = models.TextField(max_length=255,null=True)
    price = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(customusers, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    no_of_days = models.IntegerField()
    day = models.DateTimeField(auto_now_add=True)
    Total_cost = models.CharField(max_length=255,)
    booking_date = models.DateField()
    status = models.CharField(default='pending',max_length=255)

    def __str__(self):
        return self.car.name






