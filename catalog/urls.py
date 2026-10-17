from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, category, product

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contact/', contacts, name='contact'),
    path('category/', category, name='category'),
    path('product/', product, name='product'),

]
