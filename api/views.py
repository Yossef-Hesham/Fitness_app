from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from  django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterView(generics.CreateAPIView):
    
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)


class UserloginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserRegisterSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    
from rest_framework.pagination import PageNumberPagination
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class PaginationConfig(PageNumberPagination):
    page_size = 10  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow clients to set the page size
    max_page_size = 100  # Maximum allowed page size
class listExercisView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    # pagination_class = PaginationConfig  # Disable pagination if not needed
    # Set the number of items per page
    
    
    @method_decorator(cache_page(60*15, key_prefix='equipment')) # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        print("Fetching exercises from the cache...")
        return super().list(request, *args, **kwargs)
    
    
    def get_queryset(self):
        print("Fetching exercises from the database...")
        import time
        time.sleep(2)  # Simulate a delay for testing purposes
        return super().get_queryset()

    


