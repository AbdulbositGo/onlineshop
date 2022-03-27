from store.models import Category, SubCategory, Product

def categories(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    daily_products = Product.objects.filter().order_by("-updated")[:6]
    max_price = Product.objects.all().order_by("-price").first()
    
    context = {
        "categories": categories,
        "subcategories": subcategories,
        "daily_products": daily_products,
        "max_price": max_price
    }
    return context