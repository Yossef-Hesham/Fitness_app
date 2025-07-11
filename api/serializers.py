from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *
from django.db import transaction

from .serializers import *



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password', 'date_of_birth', 'height_cm', 'current_weight_kg']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)  # 🔐 Hash the password
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
  
        
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Email and password are required.")

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid credentials.")

        attrs['user'] = user
        return attrs 
    


class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    muscles = serializers.SlugRelatedField(slug_field='name', queryset=MuscleGroup.objects.all(), many=True)
    equipment = serializers.SlugRelatedField(slug_field='name', queryset=Equipment.objects.all(), many=True)

    class Meta:
        model = Exercise
        fields = '__all__'
        