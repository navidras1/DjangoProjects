from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from cart.cart import Cart
from ecom.models import Product


# Create your views here.

def index (request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'ecom/index.html',context)

def detail (request, slug):

    product = Product.objects.get(slug=slug)

    context = {'product':product}

    return  render(request, "ecom/detail.html", context)

@require_POST
def addToCart(request):
    cart = Cart(request)

    # product = Product.objects.get(id=request.POST['product_id'])
    product = get_object_or_404(Product, id=request.POST['product_id'])
    print(f"addToCart {request.POST}")
    productId = request.POST['product_id']
    quantity = request.POST['quantity']
    cart.add(product,quantity)


    print( request.session['cart'])
    print(cart.__len__())

    return JsonResponse({
        'success': True,
        'product_id': productId,
        'quantity': quantity,
        'cart_count': cart.__len__(),
        'message': f'Product {productId} (x{quantity}) added to cart and total objects are {cart.__len__()}',
    })
