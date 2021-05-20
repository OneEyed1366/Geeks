from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum, Count
from auth_app.models import User
from main.models import Product, Category
from main.forms import CategoryRegisterForm, CategoryEditForm
from .forms import UserAdminEditForm
from auth_app.forms import UserRegisterForm

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    content = {
        'users': User.objects.all().count(),
        'products': Product.objects.all().count(),
        'categories': Category.objects.all().count(),
    }
    return render(request, "admin_app/index.html", context = content)

def users(request):
    title = 'Админ.панель/Пользователи'
    users_list = User.objects.all().order_by(
        '-is_active', '-is_superuser', '-is_staff', 'username')
    content = {
        'title': title,
        'datas': users_list
    }

    return render(request, 'admin_app/users/index.html', content)


def user_create(request):
    title = 'Пользователи - Создание пользователя'
    content = {'title': title, 'update_form': ''}

    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users:index'))
    else:
        form = UserRegisterForm()

    content["update_form"] = form

    return render(request, 'admin_app/users/create-update.html', content)


def user_update(request, pk):
    title = 'Пользователи - Редактирование пользователя'
    to_edit = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        edit_form = UserAdminEditForm(
            request.POST, request.FILES, instance=to_edit)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(
                reverse('admin:users:update', args=[to_edit.pk]))
    else:
        edit_form = UserAdminEditForm(instance=to_edit)
    
    content = {'title': title, 'update_form': edit_form}
    
    return render(request, 'admin_app/users/create-update.html', context = content)


def user_delete(request, pk):
    title = 'Пользователи - Удаление пользователя'
    to_delete = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        #to_delete.delete()
        #вместо удаления лучше сделаем неактивным
        to_delete.is_active = False
        to_delete.save()

        return HttpResponseRedirect(reverse('admin:users:read'))

    content = {'title': title, 'user_to_delete': to_delete}

    return render(request, 'admin_app/users/delete.html', content)


def categories(request):
    title = 'Админ.панель/Категории товаров'
    categories_list = Category.objects.all()
    content = {
        'title': title,
        'datas': categories_list
    }

    return render(request, 'admin_app/categories/index.html', content)

def category_create(request, pk):
    content = {'title': title, 'category': Category.objects.get(pk=pk)}

    if request.method == 'POST':
        form = CategoryRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:users:index'))
    else:
        form = UserRegisterForm()

    content["update_form"] = form

    return render(request, 'admin_app/categories/create-update.html', content)

def category_update(request, pk):
    content = {
        "title": "Категории - Редактирование категорий",
        "category": Category.objects.get(pk=pk),
    }
    to_edit = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        edit_form = CategoryEditForm(
            request.POST, request.FILES, instance=to_edit)

        if edit_form.is_valid():
            edit_form.save()

            return HttpResponseRedirect(
                reverse('admin:categories:update', args=[to_edit.pk]))
    else:
        edit_form = CategoryEditForm(instance=to_edit)

    content["update_form"] = edit_form

    return render(request, 'admin_app/categories/create-update.html', context=content)

def category_delete(request, pk):
    to_delete = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        #to_delete.delete()
        #вместо удаления лучше сделаем неактивным
        to_delete.is_active = False
        to_delete.save()

        return HttpResponseRedirect(reverse('admin:categories:read'))

    content = {'title': "Категории - Удаление категории", 'to_delete': to_delete}

    return render(request, 'admin_app/categories/delete.html', content)

def products(request, pk):
    title = 'Админ.панель/Товары'
    category = get_object_or_404(Category, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('title')

    content = {
        'title': title,
        'category': category,
        'datas': products_list,
    }

    return render(request, 'admin_app/products/index.html', context = content)


def product_create(request, pk):
    pass


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass
