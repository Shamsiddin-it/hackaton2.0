from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=15, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    lat = models.DecimalField(max_digits=9, decimal_places=6)  # Latitude
    lon = models.DecimalField(max_digits=9, decimal_places=6)  # Longitude
    available = models.BooleanField(default=True)  # Track if car is available
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.number})"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    place_of_order = models.CharField(max_length=255)
    place_of_return = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default='pending')  # Can be 'pending', 'confirmed', 'completed'

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_start = models.DateTimeField()
    rental_end = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} rented {self.car.title}"


class CarLocationHistory(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Car {self.car.title} location at {self.timestamp}"
