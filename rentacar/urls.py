from django.urls import path
from .views import *

urlpatterns = [
    # Company URLs
    path('companies/', CompanyAPIView.as_view(), name='company-list'),
    path('companies/create/', CompanyCreateAPIView.as_view(), name='company-create'),
    path('companies/<int:pk>/', CompanyRetrieveAPIView.as_view(), name='company-detail'),
    path('companies/<int:pk>/update/', CompanyRetrieveUpdateAPIView.as_view(), name='company-update'),
    path('companies/<int:pk>/delete/', CompanyRetrieveDestroyAPIView.as_view(), name='company-delete'),

    # Car URLs
    path('cars/', CarAPIView.as_view(), name='car-list'),
    path('cars/create/', CarCreateAPIView.as_view(), name='car-create'),
    path('cars/<int:pk>/', CarRetrieveAPIView.as_view(), name='car-detail'),
    path('cars/<int:pk>/update/', CarRetrieveUpdateAPIView.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', CarRetrieveDestroyAPIView.as_view(), name='car-delete'),

    # Order URLs
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateAPIView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order-detail'),
    path('orders/<int:pk>/update/', OrderRetrieveUpdateAPIView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderRetrieveDestroyAPIView.as_view(), name='order-delete'),

    # My Rented Cars (orders specific to logged-in user)
    path('my-rented-cars/', MyRentedCars.as_view(), name='my-rented-cars'),
    path('orders/<int:pk>/end-rental/', OrderEndRentalAPIView.as_view(), name='order-end-rental'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    
    # Login
    path('login/', LoginUserAPIView.as_view(), name='login'),
    
    # Logout
    path('logout/', LogoutUserAPIView.as_view(), name='logout'),
]
