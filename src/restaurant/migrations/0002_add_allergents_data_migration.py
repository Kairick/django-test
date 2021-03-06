# Generated by Django 4.0.4 on 2022-05-29 18:53

from django.db import migrations


def add_default_allergens(apps, schema_editor):
    """Добавляет аллергены в базу"""
    allergens = [
        'Молоко', 'Яйцо', 'Рыба', 'Какао', 'Зерно', 'Цитрусовые', 'Орехи'
    ]
    Allergen = apps.get_model('restaurant', 'Allergen')
    items = [Allergen(name=allergen) for allergen in allergens]
    Allergen.objects.bulk_create(items)


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_allergens),
    ]
