from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restaurant.models import Menu

#Menu View test
class MenuItemsViewTest(APITestCase):
    def setUp(self):
        """adding some instance of menu model and user with is token"""
        #menu instances
        self.menu_1 = Menu.objects.create(title='salad', price=2.5, inventory=4)
        self.menu_2 = Menu.objects.create(title='jus', price= 3, inventory=6)
        self.menu_3 = Menu.objects.create(title='pasta', price=5, inventory=8)
        
        #user instance
        self.username = 'user_name'
        self.password  = 'user_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token'+self.token.key)
        
    def test_getall(self):
        """retrieve all objects"""
        response = self.client.get('/api/menu-items')
        self.assertEqual(response.status_code, 200)
        
        expected_data =[
            {"id": 2, "title":"salad", "price": "2.50", "stock": 4},
            {"id": 3,"title":"jus", "price": "3.00", "stock": 6},
            {"id": 4, "title":"pasta", "price": "5.00", "stock": 8},
        ]
        
        self.assertEqual(response.json(), expected_data)