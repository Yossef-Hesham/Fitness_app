from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .serializers import *
from .models import *
from rest_framework.response import Response
from   django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# from rest_framework.status 

# Create your views here.
