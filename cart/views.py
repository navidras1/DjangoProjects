from django.http import request
from django.shortcuts import render
from django.http import JsonResponse
from .cart import Cart


# Create your views here.
def cartoverview(request):

    cart = Cart(request)
    return render(request, 'cartOverview.html', {'cart':cart})

def update_cart(request):
    cart = Cart(request)
    quantity=request.POST['quantity']
    product_id=request.POST['product_id']
    cart.update(product_id,quantity)
    return  JsonResponse({'success':True})

def delete_cart(request):
    cart = Cart(request)
    product_id=request.POST['product_id']
    cart.remove_item(product_id)
    return JsonResponse({'success': True})

def clear(request):
    cart = Cart(request)
    cart.clear()
    return JsonResponse({'success':True})
