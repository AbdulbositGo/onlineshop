from django.core.paginator import Paginator
from django.db.models import Q

def min_max_filter(request, products):
    min_price = request.GET.get("min", None)
    max_price = request.GET.get("max", None)

    if min_price:
        products = products.filter(price__gte=min_price)
    
    if max_price:
        products = products.filter(price__lte=max_price)

    return products


def get_paginated(request, items, number):
    page = request.GET.get("page")

    items = min_max_filter(request, items)
    items_len = len(items)
    pages = Paginator(items, number)
    items = pages.get_page(page)


    return {
        "items": items,
        "items_len": items_len,
        "pages": pages
    }

def search_item(request, items):
    text = request.GET.get("search")    
    if text:
        return items.filter(Q(name__icontains=text) | Q(description__icontains=text)).order_by("?")
    
    return items