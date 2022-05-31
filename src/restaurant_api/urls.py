from django.urls import path

from restaurant_api.views import DishCreateView

urlpatterns = [
    path('new/', DishCreateView.as_view(), name="create_dish"),
    ]