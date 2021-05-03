from django.shortcuts import render
from .models import Product

def index(request):
    data = {
        "products": Product.objects.all(),
    }

    return render(request, "index.html", context = data)

def products(request):
    data = {
        "products": Product.objects.all(),
    }

    return render(request, 'products.html', context = data)

def contact(request):
    return render(request, 'contact.html')