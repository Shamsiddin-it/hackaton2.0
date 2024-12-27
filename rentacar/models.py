from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    year = models.IntegerField()
    COLOR = (
        ('red', 'red'),
        ('yellow', 'yellow'),
        ('black', 'black'),
        ('green', 'green'),
        ('white', 'white'),
        ('other', 'other'),
    )
    color = models.CharField(choices=COLOR, max_length=50)
    number = models.CharField(max_length=8)
    renta_daily = models.DecimalField(max_digits=8, decimal_places=2)
    per_minute = models.IntegerField()
    
    def __str__(self):
        return self.model
                        
class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    days = models.IntegerField()
    minutes = models.IntegerField()
    ordered_on = models.DateTimeField(auto_now_add=True)  
    returned_on = models.DateTimeField(null=True, blank=True)  

    def __str__(self):
        return str(self.car)

    def rental_duration_in_minutes(self):
        if self.returned_on:
            duration = self.returned_on - self.ordered_on
            return duration.total_seconds() / 60
        else:
            return None 

