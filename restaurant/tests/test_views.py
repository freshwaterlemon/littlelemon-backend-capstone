# restaurant/tests/test_views.py
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User


class MenuViewTest(APITestCase):
    def setUp(self):
        # Create test user and authenticate
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create test data
        Menu.objects.create(title="Bruschetta", price=8.99, inventory=15)
        Menu.objects.create(title="Tiramisu", price=6.50, inventory=10)

    def test_getall(self):
        url = reverse("menu-list")
        response = self.client.get(url)

        # Verify status code
        self.assertEqual(response.status_code, 200)

        # Verify data count
        self.assertEqual(len(response.data), 2)

        # Verify serialized data matches
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_menu_item(self):
        url = reverse("menu-list")
        data = {"title": "Lasagna", "price": 14.99, "inventory": 25}
        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 3)
