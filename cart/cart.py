from django.conf import settings
from product.models import Product

class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # initialize empty cart if no cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        # get product ids from cart
        product_ids = self.cart.keys()
        # get products from db
        products = Product.objects.filter(id__in=product_ids)
        # populate cart with product objects
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['total_price'] = item['quantity'] * item['product'].price
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product_id):
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

            
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        return sum(item.get('total_price', 0) for item in self.cart.values())

    
    def get_item(self, product_id):
        if str(product_id) in self.cart:
            return self.cart[str(product_id)]
        return None
