from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, Count
from auth_app.models import User
from main.models import Product, Category
from main.forms import CategoryRegisterForm, CategoryEditForm, ProductEditForm
from .forms import UserAdminEditForm
from auth_app.forms import UserRegisterForm

class UsersListView(ListView):
    model = User
    template_name = 'admin_app/users/_index.html'
    
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductsCreateView(CreateView):
    model = Product
    template_name = 'admin_app/products/create-update.html'
    success_url = reverse_lazy('admin:products:create')
    fields = '__all__'

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'admin_app/categories/create-update.html'
    success_url = reverse_lazy('admin:categories:create')
    fields = '__all__'

class UsersCreateView(CreateView):
    model = User
    template_name = 'admin_app/users/create-update.html'
    success_url = reverse_lazy('admin:users:create')
    fields = '__all__'
    
class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'admin_app/categories/create-update.html'
    success_url = reverse_lazy('admin:categories:update')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории - Редактировать категории'
        
        return context

class UsersUpdateView(UpdateView):
    model = User
    template_name = 'admin_app/users/create-update.html'
    success_url = reverse_lazy('admin:users:update')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи - Редактировать пользователя'
        
        return context

class ProductsUpdateView(UpdateView):
    model = Product
    template_name = 'admin_app/products/create-update.html'
    success_url = reverse_lazy('admin:products:update')
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары - Редактировать товар'
        context["category"] = context["object"].category
        
        return context

class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admin_app/products/delete.html'
    success_url = reverse_lazy('admin:products:delete')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admin_app/categories/delete.html'
    success_url = reverse_lazy('admin:categories:delete')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class UsersDeleteView(DeleteView):
    model = User
    template_name = 'admin_app/users/delete.html'
    success_url = reverse_lazy('admin:users:delete')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

        
class ProductDetailView(DetailView):
    model = Product
    template_name = 'admina_pp/products/read.html' 

@user_passes_test(lambda u: u.is_superuser)
def index(request):
    content = {
        'users': User.objects.all().count(),
        'products': Product.objects.all().count(),
        'categories': Category.objects.all().count(),
    }
    return render(request, "admin_app/index.html", context = content)

def categories(request):
    title = 'Админ.панель/Категории товаров'
    categories_list = Category.objects.all()
    content = {
        'title': title,
        'datas': categories_list
    }

    return render(request, 'admin_app/categories/_index.html', content)

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