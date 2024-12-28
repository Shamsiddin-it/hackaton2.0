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

# serializers.py
# serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'email', 'first_name', 'last_name']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')  # Remove the password_confirm field
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        return user


from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid username or password.')

        # You can return the authenticated user if needed (e.g., for logging in)
        data['user'] = user
        return data