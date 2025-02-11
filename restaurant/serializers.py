from rest_framework import serializers
from .models import Menu, Booking
from rest_framework.validators import UniqueValidator

#User serialazer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'stock']
        
        #data validation
        extra_kwargs = {
            'title' : {'validators': [UniqueValidator(
                queryset=Menu.objects.all()             #unique validation
            )]},
            'price' : {'min_value': 2}, #minimum value
            'stock': {'source': 'inventory', 'min_value': 0}
        }
        
#Booking Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        extra_kwargs = {
            'no_of_guests': {'min_value': 1}
        }