import pytest
from django.conf import settings
from django.test import override_settings
from rest_framework.test import APIClient

from restaurant.models import Category, Dish

TEST_DIR = 'test_data'


@pytest.mark.django_db
class TestDishCreateView:
    """Тестирует DishCreateView"""
    url = '/api/menu/new/'

    @override_settings(JWT_TOKEN='1234', MEDIA_ROOT=f'{TEST_DIR}/media')
    def test_create_success(self, fake_image):
        """Тестирует успешное создание нового блюда в меню"""
        data = {
            'name': 'Борщ',
            'nutritional_value': 250,
            'price': 225.6,
            'image': fake_image,
            'category': Category.MAIN_DISH,
            'allergens': [1, 2, 3]
        }
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {settings.JWT_TOKEN}')

        response = client.post(self.url, data=data)
        dishes = Dish.objects.all()

        assert response.status_code == 201
        assert dishes.count() == 1
        assert dishes[0].name == data.get('name')
        assert dishes[0].category == Category.MAIN_DISH

    @override_settings(JWT_TOKEN='1234', MEDIA_ROOT=f'{TEST_DIR}/media')
    def test_post_with_incomplete_data(self, fake_image):
        """Тестирует поведение API при неправильном заполнении данных"""
        data = {
            'nutritional_value': 250,
            'price': 225.6,
            'image': fake_image,
            'category': Category.MAIN_DISH,
            'allergens': [1, 2, 3]
        }
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Token {settings.JWT_TOKEN}')

        response = client.post(self.url, data=data)
        dishes = Dish.objects.all()

        assert response.status_code == 400
        assert dishes.count() == 0
        assert response.json() == {'name': ['This field is required.']}

    def test_post_with_wrong_token(self):
        """Тестирует поведение API при запросе с невалидным токеном"""

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='fdfsfsfd')

        response = client.post(self.url, data={})

        assert response.status_code == 403
        assert response.json() == {
            'detail': 'Authentication credentials were not provided.'
        }
