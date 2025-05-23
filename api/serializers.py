from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.db import transaction

class ProfileInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['DateOfbirth', 'Is_coach','picture', 'Weight', 'Cardio_type']

class ProfileOutputSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'DateOfbirth', 'picture', 'Age', 'Is_coach']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile = ProfileInputSerializer()

    class Meta:
        model = User
        fields = ['user', 'profile']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        profile_data = validated_data.pop('profile')

        with transaction.atomic():
            # Create the user
            user = User.objects.create_user(
                username=user_data['username'],
                email=user_data['email'],
                password=user_data['password']
            )

            # Create the profile
            Profile.objects.create(
                user=user,
                DateOfbirth=profile_data.get('DateOfbirth'),
                Is_coach=profile_data.get('Is_coach', False),
                picture=profile_data.get('picture'),
                Weight=profile_data.get('Weight'),
                Cardio_type=profile_data.get('Cardio_type'),
                Age=profile_data.get('Age'),
            )

        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(source='exercises', many=True)

    class Meta:
        model = WorkoutDay
        fields = ['user', 'workout', 'date', 'exercise']  # Added 'workout' instead of typo 'Workout'

    def create(self, validated_data):
        exercise_data_list = validated_data.pop('exercises')
        workout = WorkoutDay.objects.create(**validated_data)
        for data_list in exercise_data_list:
            Exercise.objects.create(Workout=workout, **data_list)
        return workout
    
