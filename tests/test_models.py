from django.test import TestCase
from restaurant.models import Menu

#Menu models test
class MenuItemsTest(TestCase):
    def test_get_item(self):
        """test of adding a new instance of Menu model"""
        item = Menu.objects.create(title='falafel', price=4, inventory=5)
        self.assertEqual(str(item), "falafel:4")
        