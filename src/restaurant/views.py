import json

from django.shortcuts import redirect, render

from restaurant.models import Category, Dish


def all_dishes(request):
    """Представление для списка блюд в меню"""
    dishes = Dish.objects.all()
    if request.method == "POST":
        id_list = request.POST.getlist('dishes_id')
        id_list = [int(i) for i in id_list]

        return redirect('restaurant:orders', dish_ids=id_list)

    return render(request, 'main.html',
                  {'dishes': dishes, 'categories': Category})


def order(request, dish_ids):
    """Представление заказа"""
    ids = json.loads(dish_ids)
    dishes = Dish.objects.filter(id__in=ids).prefetch_related('allergens')
    total = sum([dish.price for dish in dishes])

    return render(request, 'order.html', {'dishes': dishes, 'total': total})
