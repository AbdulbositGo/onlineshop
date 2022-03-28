from django.urls import path

from .views import *

urlpatterns = [
    path("cart/add-item/<int:product_id>/", add_item_view, name="add-item"),
    path("cart/reduce-item/<int:product_id>/", reduce_item_view, name="reduce-item"),
    path("cart/remove-item/<int:product_id>/", remove_item_view, name="remove-item"),
    path("cart/view", cart_view, name="cart"),
]