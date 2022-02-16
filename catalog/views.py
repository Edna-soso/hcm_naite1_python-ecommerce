from itertools import product
from django.shortcuts import render
from django.template import context
from django.utils.translation import gettext as _
from .models import *
def store(request):
    products =Product.objects.all()
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart (request):
    if request.user.is_authenticated:
        customer=request.user.customer
        order=Order.objects.get_or_create(customer=customer)
        items=order.orderitem_set.all()
    else:
        items=[]
    context={'items':items}
    return render(request, 'store/cart.html', context)

def checkout(request):
      context = {}
      return render(request, 'store/checkout.html', context)
