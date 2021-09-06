from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls.base import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from main.models import Category, Product

class ProductsListView(ListView):
    model = Product
    template_name = 'admin_app/products/_index.html'
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs["pk"]
        context = super().get_context_data(**kwargs)
        context["title"] = "Админ.панель/Товары"
        context["category"] = get_object_or_404(Category, pk=pk)
        context["datas"] = Product.objects.filter(category__pk=pk).select_related('pk')

        return context


class ProductsCreateView(CreateView):
    model = Product
    template_name = 'admin_app/products/create-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin:products:index', kwargs={"pk": super().get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары - Редактировать товар'
        context["category"] = get_object_or_404(Category, pk=self.kwargs["pk"])

        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'admin_app/products/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = context["product"]

        return context

class ProductsUpdateView(UpdateView):
    model = Product
    template_name = 'admin_app/products/create-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin:products:index', kwargs={"pk": super().get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Товары - Редактировать товар'
        context["category"] = context["object"].category

        return context

class ProductsDeleteView(DeleteView):
    model = Product
    template_name = 'admin_app/products/delete.html'

    def get_success_url(self):
        return reverse_lazy('admin:products:index', kwargs={"pk": super().get_object().category.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pk"] = super().get_object().id

        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
