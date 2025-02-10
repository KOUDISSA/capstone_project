from rest_framework import serializers
from .models import Menu
from rest_framework.validators import UniqueValidator

#User serialazer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'name', 'no_of_guests', 'booking_date']
        
        #data validation
        extra_kwargs = {
            'name' : {'validators': [UniqueValidator(
                queryset=Menu.objects.all()             #unique validation
            )]},
            'no_of_guests' : {'min_value': 1} #minimum value
        }
        