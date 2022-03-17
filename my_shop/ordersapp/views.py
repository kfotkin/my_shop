from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from .models import Order, OrderItem
from django.urls import reverse_lazy
from django.forms import inlineformset_factory
from .forms import OrderForm, OrderItemForm
from basketapp.models import Basket
from django.db import transaction


class OrderList(ListView):
    model = Order
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetail(DetailView):
    model = Order


class OrderEditMixin:
    def make_formset(self, instance=None):
        OrderFormSet = inlineformset_factory(
        Order, 
        OrderItem, 
        form=OrderItemForm, 
        extra=1
        )
        formset = OrderFormSet(instance=instance)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST, instance=instance)
        else:
            if not instance:
                basket_items = self.request.user.basket.all()
                if len(basket_items):
                    OrderFormSet = inlineformset_factory(
                        Order, 
                        OrderItem, 
                        form=OrderItemForm, 
                        extra=len(basket_items)
                        )
                    formset = OrderFormSet()
                    for num, form in enumerate(formset.forms):
                        form.initial['product'] = basket_items[num].product
                        form.initial['quantity'] = basket_items[num].quantity
                    basket_items.delete()

        return formset

    def save_formset(self, form, formset, instance=None):
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
        if not self.object.get_total_cost():
            self.object.delete()


class OrderCreate(OrderEditMixin, CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderCreate, self).get_context_data(**kwargs)
        data['orderitems'] = self.make_formset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']     
        self.save_formset(form, orderitems) 
        return super(OrderCreate, self).form_valid(form)



class OrderUpdate(OrderEditMixin, UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('ordersapp:orders_list')

    def get_context_data(self, **kwargs):
        data = super(OrderUpdate, self).get_context_data(**kwargs)
        data['orderitems'] = self.make_formset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']     
        self.save_formset(form, orderitems, instance=self.object) 
        return super(OrderUpdate, self).form_valid(form)


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('ordersapp:orders_list')  


def order_forming_complete(request):

    pass