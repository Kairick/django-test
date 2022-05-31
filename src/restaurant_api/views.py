from rest_framework.generics import CreateAPIView

from restaurant.models import Dish
from restaurant_api.permissions import JwtAuth
from restaurant_api.serializers import DishSerializer


class DishCreateView(CreateAPIView):
    """Представление для создания блюда"""
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [JwtAuth]