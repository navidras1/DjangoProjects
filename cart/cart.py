from decimal import Decimal

from ecom.models import Product


class Cart():
    def __init__(self,request):
        self.session = request.session
        self.cart = self.session.setdefault('cart', {})

    def add(self, product , quantity):
        # Session keys must be strings
        product_id = str(product.id)

        # Overwrite the quantity (replace, don't accumulate)
        self.cart[product_id] = {
            'price': str(product.price),
            'qty': quantity,
        }
        self.session.modified = True

    def __len__(self):
        # return 10
        return sum(int(item['qty']) for item in self.cart.values())
        # return len(self.cart)

    def __iter__(self):
        product_ids= self.cart.keys()
        products= Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']= product
        for item in cart.values():
            item['price']= Decimal(item['price'])
            item['total'] = Decimal(item['qty']) * item['price']
            yield item


    def total_price(self):
        return sum( Decimal( item['price'])* Decimal( item['qty']) for item in self.cart.values())

    def update(self, product_id , quantity):
        self.cart[product_id] ['qty'] = quantity
        self.session.modified = True

    def remove_item(self, product_id):
        del self.cart[product_id]
        self.session.modified = True

    def clear(self):
        self.cart.clear()
        self.session.modified = True

