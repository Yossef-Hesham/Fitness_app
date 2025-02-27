from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from   django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# from rest_framework.status 

# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileOutputSerializer
    

class RegisterView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        seralizer = self.get_serializer(data=request.data)
        
        if seralizer.is_valid():
            user = seralizer.save()
            profile = user.profile
            return Response(
                {
                    'message': 'User Registred Successfully.',
                    'profile': ProfileOutputSerializer(profile).data
                }, status= status.HTTP_201_CREATED
            )
        return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
            


class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        seralizer = self.get_serializer(data=request.data)
        if not seralizer.is_valid():
            return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        if seralizer.is_valid():
            username = seralizer.validated_data['username']
            password = seralizer.validated_data['password']
            user = authenticate(username=username, password=password)
            
            
            if not user:
                return Response(
                {'detail': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
            refresh = RefreshToken.for_user(user)
            profile = user.profile
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'profile':ProfileOutputSerializer(profile).data
                },status=status.HTTP_200_OK,
            )
                
            
    
    