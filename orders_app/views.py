from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.db import transaction

from django.forms import inlineformset_factory

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from shoppingCart_app.models import ShoppingCart as Basket
from .models import Order, OrderItem
from .forms import OrderItemForm

# @receiver(pre_save, sender=OrderItem)
# @receiver(pre_save, sender=Basket)
# def product_quantity_update_save(sender, update_fields, instance, **kwargs):
#     if update_fields == 'quantity' or 'product':
#         if instance.pk:
#             instance.product.quantity -= instance.quantity - \
#                                         sender.get_item(instance.pk).quantity
#         else:
#             instance.product.quantity -= instance.quantity
#         instance.product.save()

# @receiver(pre_delete, sender=OrderItem)
# @receiver(pre_delete, sender=Basket)
# def product_quantity_update_delete(sender, instance, **kwargs):
#     instance.product.quantity += instance.quantity
#     instance.product.save()

def index(request):
    data = {}

    return render(request, "orders_app/index.html", context=data)

def order_forming_complete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.status = Order.SENT_TO_PROCEED
    order.save()

    return HttpResponseRedirect(reverse('orders_app:orders_list'))

class OrderList(ListView):
        model = Order
        
        def get_queryset(self):
            return Order.objects.filter(user=self.request.user)

class OrderItemsCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders_app:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderItemsCreate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, \
                                            form=OrderItemForm, extra=1)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.all()
            if len(basket_items):
                OrderFormSet = inlineformset_factory(Order, OrderItem, \
                                    form=OrderItemForm, extra=len(basket_items))
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].product
                    form.initial['quantity'] = basket_items[num].quantity
                    form.initial['price'] = basket_items[num].product.product.price
                basket_items.delete()
            else:
                formset = OrderFormSet()

        data['orderitems'] = formset
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsCreate, self).form_valid(form)

class OrderItemsUpdate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders_app:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderItemsUpdate, self).get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(
            Order,
            OrderItem,
            form=OrderItemForm,
            extra=1
        )


        if self.request.POST:
            data['orderitems'] = OrderFormSet(self.request.POST, instance=self.object)
        else:
            formset = OrderFormSet(instance=self.object)
            for form in formset.forms:
                if form.instance.pk:
                    form.initial['price'] = form.instance.product.price
            data['orderitems'] = formset

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()

        # удаляем пустой заказ
        if self.object.get_total_cost() == 0:
            self.object.delete()

        return super(OrderItemsUpdate, self).form_valid(form)

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders_app:orders_list')

class OrderRead(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderRead, self).get_context_data(**kwargs)
        context['title'] = 'заказ/просмотр'

        return context
