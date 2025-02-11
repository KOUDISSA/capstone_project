from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.
#Menuitem View
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItem(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
   
#Booking view
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    