from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Order, UserHistory, CarLocationHistory
from .serializers import CarSerializer, OrderSerializer, UserHistorySerializer, CarLocationHistorySerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only available cars
        return Car.objects.filter(available=True)

    @action(detail=True, methods=['post'])
    def book_car(self, request, pk=None):
        car = self.get_object()
        # Check if car is available
        if not car.available:
            return Response({'error': 'Car not available'}, status=400)

        # Extract dates and locations from request data
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        place_of_order = request.data.get('place_of_order')
        place_of_return = request.data.get('place_of_return')

        # Create order
        order = Order.objects.create(
            car=car,
            user=request.user,
            start_date=start_date,
            end_date=end_date,
            place_of_order=place_of_order,
            place_of_return=place_of_return,
        )

        # Mark car as unavailable
        car.available = False
        car.save()

        return Response(OrderSerializer(order).data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter orders by logged-in user
        return Order.objects.filter(user=self.request.user)


class UserHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter user history by logged-in user
        return UserHistory.objects.filter(user=self.request.user)


class CarLocationHistoryViewSet(viewsets.ModelViewSet):
    queryset = CarLocationHistory.objects.all()
    serializer_class = CarLocationHistorySerializer
    permission_classes = [IsAuthenticated]
