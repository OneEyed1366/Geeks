from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from main.models import Category

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'admin_app/categories/create-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin:categories:read')

class CategoryListView(ListView):
    model: Category
    template_name = 'admin_app/categories/_index.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Админ.панель/Категории товаров"
        context["datas"] = Category.objects.all()

        return context

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'admin_app/categories/create-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin:categories:read')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категории - Редактировать категории'

        return context


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admin_app/categories/delete.html'

    def get_success_url(self):
        return reverse_lazy('admin:categories:read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
