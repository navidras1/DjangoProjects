from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from cart.cart import Cart
from .forms import AddressForm
from .models import Address, Order, OrderItem


@login_required
def checkout(request):
    # 1. Get the user's address or redirect to add-address page
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        messages.warning(request, 'Please add a delivery address before checking out.')
        return redirect('orders:add_address')

    cart = Cart(request)

    # 2. Redirect if cart is empty
    if len(cart) == 0:
        messages.info(request, 'Your cart is empty.')
        return redirect('ecom:index')

    # 3. Handle POST — create the order
    if request.method == 'POST':
        # Create the order with ONLY the fields your model has
        order = Order.objects.create(
            user=request.user,
            total_amount=cart.total_price(),
            is_paid=False,
        )

        # Create each order item
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['qty'],
            )

        # Clear the cart
        cart.clear()

        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('orders:order_success', pk=order.id)

    # 4. GET — show the checkout page
    return render(request, 'checkout.html', {
        'address': address,
        'cart': cart,
    })



@login_required
def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect("ecom:index")


    address = Address.objects.filter(user=request.user).first();
    form = AddressForm(instance=address)
    return render(request, "add_address.html", {"form": form})

@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'order_success.html', {'order': order})