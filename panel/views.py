from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rentacar.models import Car, Order, UserHistory, CarLocationHistory
from .forms import CarForm, OrderForm, UserHistoryForm, CarLocationHistoryForm

# Саҳифаи мошинҳо (Cars)
# 
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})


def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})


def car_update(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_form.html', {'form': form})


def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    car.delete()
    return redirect('car_list')

# Саҳифаи фармоишҳо (Orders)

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')   
    else:
        form = OrderForm()
    return render(request, 'order_form.html', {'form': form})


def order_update(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'order_form.html', {'form': form})


def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('order_list')

# Саҳифаи таърихи корбар (User History)

def user_history_list(request):
    histories = UserHistory.objects.all()
    return render(request, 'user_history_list.html', {'histories': histories})
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
from django.shortcuts import render
from rentacar.models import CarLocationHistory


from django.shortcuts import render
from rentacar.models import Car

def rented_cars_map(request):
    # Получаем данные о машинах
    rented_cars = Car.objects.all()

    # Передаем данные в шаблон
    return render(request, 'rented_cars_map.html', {'rented_cars': rented_cars})
