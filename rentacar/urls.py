from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'user-history', UserHistoryViewSet)
router.register(r'car-location-history', CarLocationHistoryViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
