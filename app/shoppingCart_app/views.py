from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import ShoppingCart, ShoppingCartTax
from main.models import Product


def index(request):
    data = {
        "datas": ShoppingCart.objects.all(),
        "sum": sum([item.cost for item in ShoppingCart.objects.all()]),
        "tax": ShoppingCartTax.objects.all()[0]
    }
    return render(request, "shoppingCart_app/index.html", context=data)


def add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    shopp_cart = ShoppingCart.objects.filter(
        user=request.user, product=product).first()

    if not shopp_cart:
        shopp_cart = ShoppingCart(user=request.user, product=product)

    shopp_cart.quantity += 1
    shopp_cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    shopp_cart = ShoppingCart.objects.filter(
        user=request.user, product=product).first()

    if not shopp_cart:
        shopp_cart = ShoppingCart(user=request.user, product=product)

    if shopp_cart.quantity > 0:
        shopp_cart.quantity -= 1
    shopp_cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
