from django.shortcuts import render
from django.db.models import Sum
from .models import Product, Category
from shoppingCart_app.models import ShoppingCart
from random import randrange

# slugs = [item.slug for item in Category.objects.all()]
data = {
    "cat_list": Category.objects.all(),
}


def index(request):
    data["products"] = Product.objects.all()
    data["cart"] = ShoppingCart.objects.all().aggregate(Sum("quantity"))["quantity__sum"]

    return render(request, "index.html", context=data)


def products(request, slug=None):
    data["cart"] = ShoppingCart.objects.all().aggregate(Sum("quantity"))[
        "quantity__sum"]

    if not slug:
        data["product"] = Product.objects.all()[randrange(0, len(Product.objects.all()) - 1)]
        data["products"] = Product.objects.all()
    if slug:
        data["product"] = Product.objects.filter(category__slug=slug)[
            randrange(0, len(Product.objects.filter(category__slug=slug)))]
        data["products"] = Product.objects.filter(category__slug=slug)

    return render(request, "products.html", context=data)

def products_sel(request, pk):
    data["data"] = Product.objects.get(pk=pk)
    data["cart"] = ShoppingCart.objects.all().aggregate(Sum("quantity"))[
        "quantity__sum"]
    # data["similars"] = Product.objects.filter(category__slug=)
    
    return render(request, "products_id.html", context=data)

def contact(request):
    return render(request, 'contact.html', content=data)
