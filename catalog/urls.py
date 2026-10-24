from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_list, product_detail


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contacts, name='contact'),
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),

]
