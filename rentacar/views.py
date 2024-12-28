from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car, Order, UserHistory, CarLocationHistory
from .serializers import CarSerializer, OrderSerializer, UserHistorySerializer, CarLocationHistorySerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

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
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter orders by logged-in user
        return Order.objects.filter(user=self.request.user)


class UserHistoryViewSet(viewsets.ModelViewSet):
    queryset = UserHistory.objects.all()
    serializer_class = UserHistorySerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter user history by logged-in user
        return UserHistory.objects.filter(user=self.request.user)


class CarLocationHistoryViewSet(viewsets.ModelViewSet):
    queryset = CarLocationHistory.objects.all()
    serializer_class = CarLocationHistorySerializer
    # permission_classes = [IsAuthenticated]

# views.py

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import login
from .serializers import RegisterSerializer

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(
                description="User successfully registered and logged in",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
                    }
                )
            ),
            400: 'Bad request - validation errors'
        },
        operation_description="Register a new user and log them in"
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Create the user and automatically log them in
        user = serializer.save()
        login(request, user)  # Django's built-in login method, which creates a session

        # Return the created user data (without password)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        }, status=status.HTTP_201_CREATED)


from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth import authenticate, login
from .serializers import LoginSerializer
from django.contrib.auth.models import User

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username or phone number'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            }
        ),
        responses={
            200: openapi.Response(
                description="Successful login",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
                    }
                )
            ),
            401: 'Invalid credentials'
        },
        operation_description="Authenticate user and return session-based login"
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Authenticate the user using Django's authenticate method
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user is None:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
        # Log the user in (this will create a session and set a sessionid cookie)
        login(request, user)
        
        # Optionally, return the user data (exclude password)
        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
        })

from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
