from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, '/contact.html')


def product_list(request):
    p = Product.objects.all()
    context = {'products' : p}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    p = get_object_or_404(Product, pk=pk)
    context = {"product": p}
    return render(request, 'product_detail.html', context)
