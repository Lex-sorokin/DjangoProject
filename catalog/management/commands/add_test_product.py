from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавление тестовых продуктов в БД'

    def handle(self, *args, **kwargs):
        # Удаляем данные. При необходимости можно удалить и другие модели.
        Product.objects.all().delete()
        Category.objects.all().delete()


        # Создание тестовых категорий
        cat_tv = Category.objects.create(name='Холодильники')
        cat_phone = Category.objects.create(name='Смартфоны')
        cat_furniture = Category.objects.create(name='Мебель')

        # Добавление тестовых продуктов (пример)
        Product.objects.create(
            name='Холодильник A',
            description='Двухкамерный холодильник',
            category=cat_tv,
            price=399.99,
        )
        Product.objects.create(
            name='Холодильник B',
            description='Однокамерный холодильник',
            category=cat_tv,
            price=299.99,
        )
        Product.objects.create(
            name='Смарт-전화 X',
            description='5G смартфон',
            category=cat_phone,
            price=199.99,
        )
        Product.objects.create(
            name='Стул Классик',
            description='Деревянный стул',
            category=cat_furniture,
            price=49.99,
        )

        self.stdout.write(self.style.SUCCESS('Тестовые данные добавлены.'))