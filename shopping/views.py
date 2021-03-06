from django.shortcuts import render, redirect
from django.urls import reverse

from store.models import Product
from .models import *
from .utils import get_cart



def add_item_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return redirect(reverse("store"))
    
    cart = get_cart(request)
    cart_item = CartItem.objects.filter(cart=cart, product=product).first()
    if cart_item:
        cart_item.quantity += 1
    else:
        product_price = product.price
        cart_item = CartItem(product=product, cart=cart, price=product_price)
    
    cart_item.save()

    return redirect(reverse("cart"))


def reduce_item_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return redirect(reverse("store"))
    else:
        cart = get_cart(request)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        
        if cart_item and cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

    return redirect(reverse("cart"))


def remove_item_view(request, product_id):
    product = Product.objects.filter(id=product_id).first()
    if not product:
        return redirect(reverse("store"))
    else:
        cart = get_cart(request)
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()
        if cart_item:
            cart_item.delete()
    return redirect(reverse("cart"))
    


def cart_view(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart).order_by("-created")
    cart_items_len = len(cart_items)
    if cart_items_len < 1:
        return redirect(reverse("store"))
    context = {
        "cart_items": cart_items,
    }

    return render(request, "shopping-card.html", context)