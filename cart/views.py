import re

from django.http.response import HttpResponseRedirect
from cart.forms import CartAddProductForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from main.models import Products,transactions
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

@require_POST
@csrf_exempt
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(transactions, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print(cd)
        cart.add(product=product, quantity=cd['quantity'])
    else:
        print('error')
    print(cart)

    # request.session['items_total'] = cart.product.count()
    return HttpResponseRedirect(reverse('main:home'),'success')
    # return redirect('main:home')

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(transactions, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    if not cart:
        return render(request,'main/emptycart.html')
    else:
        return render (request ,'cart/cartdetail.html',{'cart':cart})

def order_summary(request):
    cart = Cart(request)
    return render(request,'cart/orderSummary.html',{'cart':cart})
    