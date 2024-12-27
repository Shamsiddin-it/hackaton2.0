from rest_framework import serializers
from .models import Order, Car, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    rental_duration_in_minutes = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['car', 'days', 'minutes', 'total', 'username', 'rental_duration_in_minutes']

    def get_total(self, obj):
        total_cost = (obj.car.renta_daily * obj.days) 
        total_cost += (obj.car.per_minute * obj.minutes) 
        return total_cost

    def get_rental_duration_in_minutes(self, obj):
        return obj.rental_duration_in_minutes()  

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)


from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user