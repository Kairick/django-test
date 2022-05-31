from django.urls import path

from restaurant.views import all_dishes, order

urlpatterns = [
    path('', all_dishes, name="menu"),
    path('order/<dish_ids>', order, name='orders')
]
