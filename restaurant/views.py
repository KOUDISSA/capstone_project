from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#Menuitem View
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    #permission_classes = [IsAuthenticated]
    
class SingleMenuItem(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
   
#Booking view
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    