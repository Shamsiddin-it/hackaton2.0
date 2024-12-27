from rest_framework import serializers
from .models import Car, Order, UserHistory, CarLocationHistory

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'title', 'color', 'number', 'price', 'lat', 'lon', 'available']


class OrderSerializer(serializers.ModelSerializer):
    # car = CarSerializer()
    # user = serializers.StringRelatedField()  # Display the username of the user who made the order

    class Meta:
        model = Order
        fields = ['id', 'car', 'user', 'start_date', 'end_date', 'place_of_order', 'place_of_return', 'status']


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['id', 'user', 'car', 'rental_start', 'rental_end']


class CarLocationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLocationHistory
        fields = ['id', 'car', 'lat', 'lon', 'timestamp']
