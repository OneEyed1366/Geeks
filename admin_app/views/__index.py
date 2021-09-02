from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count
from auth_app.models import User
from main.models import Product, Category
from main.forms import CategoryRegisterForm, CategoryEditForm, ProductEditForm
from admin_app.forms import UserAdminEditForm
from auth_app.forms import UserRegisterForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    content = {
        'users': User.objects.all().count(),
        'products': Product.objects.all().count(),
        'categories': Category.objects.all().count(),
    }
    return render(request, "admin_app/index.html", context = content)

def products(request, pk):
    title = 'Админ.панель/Товары'
    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('title')

    content = {
        'title': title,
        'category': category,
        'datas': products_list,
    }

    return render(request, 'admin_app/products/_index.html', context = content)
