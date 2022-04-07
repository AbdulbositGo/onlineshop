from .models import *

def get_cart(request):
    session_id = request.session.session_key
    if not session_id:
        session_id = request.session.create()

    cart = Cart.objects.filter(session_id=session_id).first()
    if not cart:
        cart = Cart(session_id=session_id).save()
        cart = Cart.objects.filter(session_id=session_id).first()
    return cart


def get_quantity(request):
    cart = get_cart(request)
    items_in_cart = CartItem.objects.filter(cart=cart)
    items_quantity = 0
    if items_in_cart:
        for item in items_in_cart:
            items_quantity += item.quantity
    return items_quantity