from django.urls import path
from .views import *

urlpatterns = [
    path("", home_view, name="home"),
    path("store/", store_view, name="store"),
    path("store/<slug:category_slug>/", category_product, name="category-product"),
    path("store/<slug:category_slug>/<slug:subcategory_slug>", subcategory_product, name="subcategory-product"),
    path("store/product-detail/<product_id>/<slug>", product_detail_view, name="product-detail"),
    path("user/login", user_login_view, name="user-login-page"),
    path("user/register", user_register_view, name="user-register-page"),
]