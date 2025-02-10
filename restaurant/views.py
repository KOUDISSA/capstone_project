from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer
from .models import Menu

# Create your views here.
#Menuitem View
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
#Booking view
class SingleMenuItem(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    