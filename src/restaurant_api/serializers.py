from rest_framework import serializers

from restaurant.models import Dish


class DishSerializer(serializers.ModelSerializer):
    """Сериалайзер для блюд"""

    class Meta:
        model = Dish
        fields = (
            'name', 'nutritional_value', 'price', 'image',
            'category', 'allergens')
