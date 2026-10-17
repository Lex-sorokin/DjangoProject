from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование категории')
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name='Описание категории')


    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    description = models.TextField(max_length=150, null=True, blank=True, verbose_name='Описание товара')
    images = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Фото', help_text='Загрузите изображение товара')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория товара', help_text='Присвойте категорию', null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')


    def __str__(self):
        return f"{self.name} {self.description} {self.category} {self.price}"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', 'category']



