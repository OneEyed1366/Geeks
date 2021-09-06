from django.contrib.auth.decorators import user_passes_test
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from auth_app.models import User

class UsersCreateView(CreateView):
    model = User
    template_name = 'admin_app/users/create-update.html'
    success_url = reverse_lazy('admin:users:create')
    fields = '__all__'

class UsersListView(ListView):
    model = User
    template_name = 'admin_app/users/_index.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersUpdateView(UpdateView):
    model = User
    template_name = 'admin_app/users/create-update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin:users:update', kwargs={"pk": super().get_object().id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи - Редактировать пользователя'

        return context


class UsersDeleteView(DeleteView):
    model = User
    template_name = 'admin_app/users/delete.html'

    def get_success_url(self):
        return reverse_lazy('admin:users:delete', kwargs={"pk": super().get_object().id})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
