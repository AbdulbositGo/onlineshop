from django.shortcuts import render, get_object_or_404

from .models import *
from .utils import *


def home_view(request):
    products = Product.objects.filter().order_by("-rating")[:12]
    context={
        "products": products,
    }
    return render(request, "index.html", context)


def store_view(request):
    store_products = Product.objects.all().order_by("-created")
    store_products = search_item(request, store_products)
    
    query_string = False
    if request.GET:
        query_string = True
    paginated = get_paginated(request, store_products, 3)

    context = {
        "paginator_products": paginated["items"],
        "products_len": paginated["items_len"],
        "pages": paginated["pages"],
        "query_string": query_string
    }

    return render(request, "store.html", context)


def category_product(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    store_products = Product.objects.filter(category__category=category)
    store_products = min_max_filter(request, store_products)
    context = {
        "store_products": store_products
    }

    return render(request, "store.html", context)


def subcategory_product(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    store_products = Product.objects.filter(category__category=category, category=subcategory)
    store_products = min_max_filter(request, store_products)
    context = {
        "store_products": store_products
    }

    return render(request, "store.html", context)


def product_detail_view(request, product_id, slug):
    product_detail = Product.objects.filter(id=product_id, slug=slug).first()
    context = {
        "product_detail": product_detail
    }
    return render(request, "product_detail.html", context)


def user_login_view(request):
    return render(request, "user-login.html")


def user_register_view(request):
    return render(request, "user-register.html")