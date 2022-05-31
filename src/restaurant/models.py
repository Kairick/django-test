from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class Category(models.IntegerChoices):
    """Класс для выбора категории блюда"""
    SALAD = 1, _('Салаты')
    STARTER = 2, _('Первое блюда')
    COLD_APPETIZERS = 3, _('Холодные блюда')
    MAIN_DISH = 4, _('Горячие блюда')
    DESERTS = 5, _('Десерты')
    DRINKS = 6, _('Напитки')


class Allergen(models.Model):
    """Модель аллергенов"""
    name = models.CharField(
        verbose_name='Название аллергена', max_length=50)

    def __str__(self):
        return f'{self.name}'


class Dish(models.Model):
    """Модель блюда"""
    name = models.CharField(verbose_name='Название в меню', max_length=255)
    nutritional_value = models.PositiveSmallIntegerField(
        verbose_name='Пищевая ценность в Ккал')
    price = models.DecimalField(
        verbose_name='Цена', max_digits=8, decimal_places=2)
    image = models.ImageField(
        verbose_name="Изображение блюда",
        upload_to="uploads/restaurant/images")
    image_thumbnail = ImageSpecField(
        source='image', processors=[ResizeToFill(120, 60)],
        format='PNG', options={'quality': 60})
    category = models.PositiveSmallIntegerField(
        choices=Category.choices,
        verbose_name='Категория блюда'
    )
    allergens = models.ManyToManyField(
        Allergen,
        verbose_name="Пищевые аллергены",
        related_name="allergens"
    )

    class Meta:
        ordering = ('category',)

