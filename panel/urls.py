from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.car_list, name='car_list'),
    path('cars/create/', views.car_create, name='car_create'),
    path('cars/update/<int:pk>/', views.car_update, name='car_update'),
    path('cars/delete/<int:pk>/', views.car_delete, name='car_delete'),

    path('orders/', views.order_list, name='order_list'),
    path('orders/create/', views.order_create, name='order_create'),
    path('orders/update/<int:pk>/', views.order_update, name='order_update'),
    path('orders/delete/<int:pk>/', views.order_delete, name='order_delete'),

    path('user-history/', views.user_history_list, name='user_history_list'),
    path('map/rented_cars/', views.rented_cars_map, name='rented_cars_map'),
    
]

