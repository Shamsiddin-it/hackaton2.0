from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, OrderViewSet, UserHistoryViewSet, CarLocationHistoryViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'user-history', UserHistoryViewSet)
router.register(r'car-location-history', CarLocationHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
