from django import forms
from rentacar.models import Car, Order, UserHistory, CarLocationHistory

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['title', 'color', 'number', 'price', 'lat', 'lon', 'available']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['car', 'user', 'start_date', 'end_date', 'place_of_order', 'place_of_return', 'status']

class UserHistoryForm(forms.ModelForm):
    class Meta:
        model = UserHistory
        fields = ['user', 'car', 'rental_start', 'rental_end']

class CarLocationHistoryForm(forms.ModelForm):
    class Meta:
        model = CarLocationHistory
        fields = ['car', 'lat', 'lon']  
