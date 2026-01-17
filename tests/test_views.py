from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=20, inventory=10)
        Menu.objects.create(title="Burger", price=15, inventory=5)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)