from store.models import Category, SubCategory, Product
from shopping.utils import *

def need_context(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated")[:6]
    max_price = Product.objects.all().order_by("-price").first()    

    items_quantity = get_quantity(request)

    context = {
        "categories": categories,
        "subcategories": subcategories,
        "daily_products": daily_products,
        "max_price": max_price,
        "items_quantity": items_quantity,
    }
    return context