# restaurant/tests/test_models.py
from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_create_menu_item(self):
        item = Menu.objects.create(title="Margherita Pizza", price=12.99, inventory=20)
        self.assertEqual(str(item), "Margherita Pizza : 12.99")

    def test_default_inventory(self):
        item = Menu.objects.create(title="Fries", price=4.99)
        self.assertEqual(item.inventory, 0)  # Testing default value
